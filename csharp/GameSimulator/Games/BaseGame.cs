using System;

namespace GameSimulator
{
    public abstract class BaseGame : IGame
    {
        public string Name { get; }
        public string Genre { get; }
        public bool IsInstalled { get; private set; }
        public bool IsRunning { get; private set; }
        public bool IsLoggedIn { get; private set; }
        public HardwareSpecs HardwareRequirements { get; }
        public int SaveSlotsCount { get; private set; } = 0;

        public event EventHandler<GameEventArgs>? OnStateChanged;

        protected BaseGame(string name, string genre, HardwareSpecs requirements)
        {
            Name = name;
            Genre = genre;
            HardwareRequirements = requirements;
        }

        protected void RaiseEvent(string message)
        {
            OnStateChanged?.Invoke(this, new GameEventArgs($"[{Name}] {message}"));
        }

        public void Install(HardDrive drive)
        {
            if (IsInstalled)
            {
                RaiseEvent("Гра вже інстальована.");
                return;
            }

            if (drive.AllocateSpace(HardwareRequirements.SizeOnHddGb))
            {
                IsInstalled = true;
                RaiseEvent("Успішно інстальовано.");
            }
            else
            {
                RaiseEvent("Помилка інсталяції: Недостатньо місця на HDD!");
            }
        }

        public virtual void Launch(HardwareSpecs currentSpecs, PlatformType platform)
        {
            if (!IsInstalled)
            {
                RaiseEvent("Не можна запустити неінстальовану гру!");
                return;
            }
            if (IsRunning)
            {
                RaiseEvent("Гра вже запущена.");
                return;
            }
            if (!currentSpecs.MeetsRequirements(HardwareRequirements))
            {
                RaiseEvent("Неможливо запустити: залізо не відповідає мінімальним вимогам!");
                return;
            }

            IsRunning = true;
            RaiseEvent("Гру успішно запущено.");
        }

        public void Login(string username)
        {
            if (!IsRunning)
            {
                RaiseEvent("Неможливо увійти в акаунт: гра не запущена!");
                return;
            }
            IsLoggedIn = true;
            RaiseEvent($"Користувач {username} успішно увійшов у систему.");
        }

        public void SaveProgress()
        {
            if (!IsRunning || !IsLoggedIn)
            {
                RaiseEvent("Дія заблокована: спочатку запустіть гру та увійдіть в акаунт!");
                return;
            }
            SaveSlotsCount++;
            RaiseEvent($"Прогрес збережено. Слотів збереження: {SaveSlotsCount}");
        }

        public void LoadProgress()
        {
            if (!IsRunning || !IsLoggedIn)
            {
                RaiseEvent("Дія заблокована: спочатку запустіть гру та увійдіть в акаунт!");
                return;
            }
            if (SaveSlotsCount == 0)
            {
                RaiseEvent("Помилка завантаження: немає збережених станів!");
                return;
            }
            RaiseEvent("Прогрес успішно завантажено.");
        }

        public void Close()
        {
            if (!IsRunning) return;
            IsRunning = false;
            IsLoggedIn = false;
            RaiseEvent("Гру закрито. Сесію завершено.");
        }
    }
}
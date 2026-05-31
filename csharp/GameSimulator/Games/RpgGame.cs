namespace GameSimulator
{
    public class RpgGame : BaseGame
    {
        public bool IsMultiplayerActive { get; private set; }

        public RpgGame(string name, HardwareSpecs requirements) : base(name, "RPG", requirements) { }

        public void SetupMultiplayer(int controllersCount)
        {
            if (!IsRunning || !IsLoggedIn)
            {
                RaiseEvent("Дія заблокована: мультиплеєр налаштовується тільки всередині гри!");
                return;
            }

            if (controllersCount > 1)
            {
                IsMultiplayerActive = true;
                RaiseEvent($"Мультиплеєр активовано! Підключено маніпуляторів: {controllersCount}.");
            }
            else
            {
                IsMultiplayerActive = false;
                RaiseEvent("Мультиплеєр недоступний: потрібно підключити як мінімум 2 маніпулятори.");
            }
        }
    }
}
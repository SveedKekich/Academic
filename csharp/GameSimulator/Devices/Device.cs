using System;

namespace GameSimulator
{
    public class Device
    {
        public string ModelName { get; }
        public HardwareSpecs Specs { get; }
        public HardDrive Drive { get; }
        public PlatformType Platform { get; }
        public int ConnectedControllers { get; private set; }
        public IGame? CurrentGame { get; private set; }

        public event EventHandler<GameEventArgs>? OnDeviceLog;

        public Device(string name, PlatformType platform, HardwareSpecs specs, int initialHdd)
        {
            ModelName = name;
            Platform = platform;
            Specs = specs;
            Drive = new HardDrive(initialHdd);
        }

        public void ConnectControllers(int count)
        {
            ConnectedControllers = count;
            OnDeviceLog?.Invoke(this, new GameEventArgs($"[{ModelName}] Підключено маніпуляторів: {count}"));
        }

        public void StreamToDevice(Device targetDevice)
        {
            if (this.Platform != PlatformType.Mobile)
            {
                OnDeviceLog?.Invoke(this, new GameEventArgs($"[{ModelName}] Стрімінг екрану доступний тільки з мобільних пристроїв!"));
                return;
            }
            OnDeviceLog?.Invoke(this, new GameEventArgs($"[{ModelName}] Трансляцію екрану успішно запущено на пристрій {targetDevice.ModelName}."));
        }

        public void InstallGame(IGame game)
        {
            game.Install(Drive);
        }

        public void PlayGame(IGame game, string username)
        {
            if (CurrentGame != null && CurrentGame.IsRunning)
            {
                OnDeviceLog?.Invoke(this, new GameEventArgs($"[{ModelName}] Помилка! Спочатку закрийте активну гру: {CurrentGame.Name}"));
                return;
            }

            game.Launch(Specs, Platform);
            
            if (game.IsRunning)
            {
                CurrentGame = game;
                game.Login(username);
            }
        }

        public void StopCurrentGame()
        {
            if (CurrentGame != null && CurrentGame.IsRunning)
            {
                CurrentGame.Close();
                CurrentGame = null;
            }
        }
    }
}
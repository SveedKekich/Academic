using System;

namespace GameSimulator
{
    public interface IGame
    {
        string Name { get; }
        string Genre { get; }
        bool IsInstalled { get; }
        bool IsRunning { get; }
        bool IsLoggedIn { get; }
        HardwareSpecs HardwareRequirements { get; }
        int SaveSlotsCount { get; }
        
        event EventHandler<GameEventArgs> OnStateChanged;

        void Install(HardDrive drive);
        void Launch(HardwareSpecs currentSpecs, PlatformType platform);
        void Login(string username);
        void SaveProgress();
        void LoadProgress();
        void Close();
    }
}
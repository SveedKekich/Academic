using System;

namespace GameSimulator
{
    // Окремий клас виведення на консоль (Принцип SRP та Loose Coupling)
    public static class ConsoleNotificationService
    {
        public static void SubscribeToGame(IGame game)
        {
            game.OnStateChanged += (sender, e) => Console.WriteLine(e.Message);
        }

        public static void SubscribeToDevice(Device device)
        {
            device.OnDeviceLog += (sender, e) => Console.WriteLine(e.Message);
        }
    }
}
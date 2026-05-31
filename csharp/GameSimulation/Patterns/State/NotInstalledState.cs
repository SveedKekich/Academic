using GameSimulation.Domain;
using GameSimulation.Domain.Enums;
using GameSimulation.Domain.Models;

namespace GameSimulation.Patterns.State
{
    public class NotInstalledState : IGameState
    {
        public void Install(Game context, Device device)
        {
            if (!context.Compatibility.IsCompatible(device.Platform))
            {
                context.Notify("Ця гра несумісна з даною платформою!", GameNotificationType.Error);
                return;
            }

            if (device.AvailableHddSpaceGb < context.Requirements.HddSpaceGb)
            {
                context.Notify("Недостатньо місця на HDD для встановлення гри.", GameNotificationType.Error);
                return;
            }

            device.AvailableHddSpaceGb -= context.Requirements.HddSpaceGb;
            context.ChangeState(new InstalledState());
            context.Notify($"Гру успішно інстальовано. Використано {context.Requirements.HddSpaceGb} GB.", GameNotificationType.Success);
        }

        public void Launch(Game context, Device device) => context.Notify("Неможливо запустити. Гра ще не інстальована.", GameNotificationType.Error);
        public void Login(Game context) => context.Notify("Неможливо увійти в акаунт. Гра не запущена.", GameNotificationType.Error);
        public void Save(Game context) => context.Notify("Неможливо зберегтися. Гра не запущена.", GameNotificationType.Error);
        public void Load(Game context) => context.Notify("Неможливо завантажити. Гра не запущена.", GameNotificationType.Error);
        public void Close(Game context) => context.Notify("Гра вже закрита.", GameNotificationType.Warning);
    }
}
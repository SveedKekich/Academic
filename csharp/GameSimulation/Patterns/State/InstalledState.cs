using GameSimulation.Domain;
using GameSimulation.Domain.Enums;
using GameSimulation.Domain.Models;

namespace GameSimulation.Patterns.State
{
    public class InstalledState : IGameState
    {
        public void Install(Game context, Device device) => context.Notify("Гра вже інстальована.", GameNotificationType.Warning);

        public void Launch(Game context, Device device)
        {
            var req = context.Requirements;
            var dev = device.Specs;

            if (dev.CpuCores < req.CpuCores || dev.RamGb < req.RamGb || dev.VramGb < req.VramGb)
            {
                context.Notify("Апаратне забезпечення пристрою не відповідає мінімальним вимогам гри!", GameNotificationType.Error);
                return;
            }

            context.ChangeState(new LaunchedState());
            context.Notify("Гру успішно запущено. Будь ласка, виконайте вхід в обліковий запис.", GameNotificationType.Success);
        }

        public void Login(Game context) => context.Notify("Неможливо увійти. Гра не запущена.", GameNotificationType.Error);
        public void Save(Game context) => context.Notify("Неможливо зберегтися. Гра не запущена.", GameNotificationType.Error);
        public void Load(Game context) => context.Notify("Неможливо завантажити. Гра не запущена.", GameNotificationType.Error);
        public void Close(Game context) => context.Notify("Гра не запущена.", GameNotificationType.Warning);
    }
}
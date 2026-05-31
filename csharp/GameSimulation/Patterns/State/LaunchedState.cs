using GameSimulation.Domain;
using GameSimulation.Domain.Enums;
using GameSimulation.Domain.Models;

namespace GameSimulation.Patterns.State
{
    public class LaunchedState : IGameState
    {
        public void Install(Game context, Device device) => context.Notify("Неможливо інсталювати. Гра зараз запущена.", GameNotificationType.Error);
        public void Launch(Game context, Device device) => context.Notify("Гра вже запущена.", GameNotificationType.Warning);

        public void Login(Game context)
        {
            context.IsLoggedIn = true;
            context.Notify("Вхід в обліковий запис виконано успішно! Тепер ви можете грати.", GameNotificationType.Success);
        }

        public void Save(Game context)
        {
            if (!context.IsLoggedIn)
            {
                context.Notify("Потрібно увійти в акаунт перед збереженням.", GameNotificationType.Error);
                return;
            }
            context.HasSaves = true;
            context.Notify("Поточний стан гри успішно збережено.", GameNotificationType.Success);
        }

        public void Load(Game context)
        {
            if (!context.IsLoggedIn)
            {
                context.Notify("Потрібно увійти в акаунт перед завантаженням.", GameNotificationType.Error);
                return;
            }
            if (!context.HasSaves)
            {
                context.Notify("Немає збережених станів для завантаження.", GameNotificationType.Warning);
                return;
            }
            context.Notify("Збережений стан гри завантажено.", GameNotificationType.Success);
        }

        public void Close(Game context)
        {
            context.IsLoggedIn = false; 
            context.ChangeState(new InstalledState());
            context.Notify("Гру закрито. Повернення до стану 'Інстальовано'.", GameNotificationType.Info);
        }
    }
}
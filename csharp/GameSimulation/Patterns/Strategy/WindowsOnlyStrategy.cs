using GameSimulation.Domain.Enums;

namespace GameSimulation.Patterns.Strategy
{
    public class WindowsOnlyStrategy : ICompatibilityStrategy
    {
        public bool IsCompatible(DevicePlatform platform) => platform == DevicePlatform.WindowsPC;
    }
}
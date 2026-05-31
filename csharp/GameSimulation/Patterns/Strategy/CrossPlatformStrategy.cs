using GameSimulation.Domain.Enums;

namespace GameSimulation.Patterns.Strategy
{
    public class CrossPlatformStrategy : ICompatibilityStrategy
    {
        public bool IsCompatible(DevicePlatform platform) => true;
    }
}
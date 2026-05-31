using GameSimulation.Domain.Enums;

namespace GameSimulation.Patterns.Strategy
{
    public interface ICompatibilityStrategy
    {
        bool IsCompatible(DevicePlatform platform);
    }
}
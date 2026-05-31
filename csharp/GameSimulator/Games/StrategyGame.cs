namespace GameSimulator
{
    public class StrategyGame : BaseGame
    {
        public StrategyGame(string name, HardwareSpecs requirements) : base(name, "Стратегія", requirements) { }

        public override void Launch(HardwareSpecs currentSpecs, PlatformType platform)
        {
            if (platform != PlatformType.WindowsPC)
            {
                RaiseEvent("Критична помилка: Стратегії доступні ТІЛЬКИ на Windows PC!");
                return;
            }
            base.Launch(currentSpecs, platform);
        }
    }
}
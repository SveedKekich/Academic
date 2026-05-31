using System;
using GameSimulation.Domain.Enums;

namespace GameSimulation.Domain.Models
{
    public class Device
    {
        public DevicePlatform Platform { get; private set; }
        public HardwareSpecs Specs { get; private set; }
        public int AvailableHddSpaceGb { get; set; }

        public Device(DevicePlatform platform, HardwareSpecs specs)
        {
            Platform = platform;
            Specs = specs;
            AvailableHddSpaceGb = specs.HddSpaceGb;
        }

        public void StreamToOtherDevice()
        {
            if (Platform == DevicePlatform.Mobile)
            {
                Console.WriteLine("[Device UI] Трансляція екрану мобільного пристрою на інший екран активована.");
            }
            else
            {
                Console.WriteLine("[Device UI] Трансляція доступна лише для мобільних пристроїв.");
            }
        }
    }
}
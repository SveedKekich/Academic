namespace GameSimulation.Domain.Models
{
    public class HardwareSpecs
    {
        public int CpuCores { get; set; }
        public int RamGb { get; set; }
        public int VramGb { get; set; }
        public int HddSpaceGb { get; set; }

        public HardwareSpecs(int cpu, int ram, int vram, int hdd)
        {
            CpuCores = cpu;
            RamGb = ram;
            VramGb = vram;
            HddSpaceGb = hdd;
        }
    }
}
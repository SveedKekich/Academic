namespace GameSimulator
{
    public class HardwareSpecs
    {
        public int CpuCores { get; set; }
        public int RamGb { get; set; }
        public int VramGb { get; set; }
        public int SizeOnHddGb { get; set; }

        public HardwareSpecs(int cpu, int ram, int vram, int hdd)
        {
            CpuCores = cpu;
            RamGb = ram;
            VramGb = vram;
            SizeOnHddGb = hdd;
        }

        public bool MeetsRequirements(HardwareSpecs requirements)
        {
            return this.CpuCores >= requirements.CpuCores &&
                   this.RamGb >= requirements.RamGb &&
                   this.VramGb >= requirements.VramGb;
        }
    }
}
namespace GameSimulator
{
    // Клас керування жорстким диском (Single Responsibility)
    public class HardDrive
    {
        public int TotalCapacityGb { get; private set; }
        public int FreeSpaceGb { get; private set; }

        public HardDrive(int totalCapacityGb)
        {
            TotalCapacityGb = totalCapacityGb;
            FreeSpaceGb = totalCapacityGb;
        }

        public bool AllocateSpace(int sizeGb)
        {
            if (FreeSpaceGb >= sizeGb)
            {
                FreeSpaceGb -= sizeGb;
                return true;
            }
            return false;
        }
    }
}
namespace StringLib
{
    public class StringBase
    {
        protected string value;

        public StringBase()
        {
            value = "";
        }

        public StringBase(string str)
        {
            value = str;
        }

        public StringBase(StringBase other)
        {
            value = other.value;
        }

        public int GetLength()
        {
            return value.Length;
        }

        public string GetValue()
        {
            return value;
        }
    }
}

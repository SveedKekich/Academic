namespace StringLib
{
    public class CharString : StringBase
    {
        public CharString() : base() { }

        public CharString(string str) : base(str) { }

        public void ReplaceChar(char oldChar, char newChar)
        {
            value = value.Replace(oldChar, newChar);
        }

        public new string GetValue()
        {
            return value;
        }
    }
}

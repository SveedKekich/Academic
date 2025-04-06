using System;
using StringLib;

class Program
{
    static void Main()
    {
        CharString myStr = new CharString("hello world");
        Console.WriteLine("Початковий рядок: " + myStr.GetValue());

        myStr.ReplaceChar('o', '0');
        Console.WriteLine("Після заміни: " + myStr.GetValue());

        Console.WriteLine("Довжина: " + myStr.GetLength());
    }
}

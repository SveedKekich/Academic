using System;

class Program
{
    static void Main()
    {
        var text = new Text();
        text.AddLine(new TextLine("Hello"));
        text.AddLine(new TextLine("world"));
        text.AddLine(new TextLine("C#"));

        text.ToUpperAll();
        Console.WriteLine("Text after ToUpper:");
        foreach (var line in text.GetLines())
        {
            Console.WriteLine(line.Content);
        }

        Console.WriteLine($"Found 'WORLD': {text.FindLine("WORLD")}");

        text.RemoveLinesOfLength(5);
        Console.WriteLine("Text after removing length 5:");
        foreach (var line in text.GetLines())
        {
            Console.WriteLine(line.Content);
        }
    }
}

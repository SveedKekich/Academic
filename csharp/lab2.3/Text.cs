using System.Collections.Generic;
using System.Linq;

public class Text
{
    private List<TextLine> lines = new List<TextLine>();

    public void AddLine(TextLine line) => lines.Add(line);

    public void RemoveLine(int index)
    {
        if (index >= 0 && index < lines.Count)
            lines.RemoveAt(index);
    }

    public void Clear() => lines.Clear();

    public void ToUpperAll()
    {
        foreach (var line in lines)
            line.ToUpper();
    }

    public int FindLine(string lineText)
    {
        return lines.Count(l => l.Content == lineText);
    }

    public void RemoveLinesOfLength(int length)
    {
        lines = lines.Where(l => l.Content.Length != length).ToList();
    }

    public IEnumerable<TextLine> GetLines() => lines;
}

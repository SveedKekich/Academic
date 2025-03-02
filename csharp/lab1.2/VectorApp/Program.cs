using System;
using VectorLibrary;

class Program
{
    static void Main()
    {
        // Використання різних конструкторів
        Vector v1 = new Vector(); // Конструктор за замовчуванням
        Vector v2 = new Vector(10, 45); // Параметризований конструктор
        Vector v3 = new Vector(v2); // Конструктор копіювання

        Console.WriteLine($"Vector v2 (Length: {v2.Length}, Angle: {v2.Angle}°)");

        v2.GetEndCoordinates(out double x, out double y);
        Console.WriteLine($"End coordinates of v2: ({x}, {y})");
    }
}

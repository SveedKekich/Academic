using System;

class Program {
    static void PrintFigureInfo(Figure fig) {
        Console.WriteLine($"Площа: {fig.Area()}, Периметр: {fig.Perimeter()}");
    }

    static void Main() {
        Figure rect = new Rectangle(0, 0, 4, 3);
        Figure circ = new Circle(5);

        Console.WriteLine("Прямокутник:");
        PrintFigureInfo(rect);

        Console.WriteLine("Коло:");
        PrintFigureInfo(circ);
    }
}

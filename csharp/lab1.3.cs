using System;

class LineSegment {
    private double x1, y1, x2, y2;

    // Конструктор за замовчуванням
    public LineSegment() {
        x1 = 0; y1 = 0; x2 = 1; y2 = 1;
    }

    // Конструктор з параметрами
    public LineSegment(double x1, double y1, double x2, double y2) {
        this.x1 = x1;
        this.y1 = y1;
        this.x2 = x2;
        this.y2 = y2;
    }

    // Конструктор копіювання
    public LineSegment(LineSegment other) {
        this.x1 = other.x1;
        this.y1 = other.y1;
        this.x2 = other.x2;
        this.y2 = other.y2;
    }

    // Метод обчислення довжини відрізка
    public double Length() {
        return Math.Sqrt(Math.Pow(x2 - x1, 2) + Math.Pow(y2 - y1, 2));
    }

    // Перевантаження оператора множення (масштабування відрізка)
    public static LineSegment operator *(LineSegment segment, double factor) {
        return new LineSegment(segment.x1, segment.y1,
                               segment.x1 + (segment.x2 - segment.x1) * factor,
                               segment.y1 + (segment.y2 - segment.y1) * factor);
    }

    // Перевантаження оператора додавання
    public static LineSegment operator +(LineSegment a, LineSegment b) {
        return new LineSegment(a.x1, a.y1, b.x2, b.y2);
    }

    // Виведення інформації про відрізок
    public void Display() {
        Console.WriteLine($"LineSegment(({x1}, {y1}) -> ({x2}, {y2})), Length: {Length()}");
    }
}

class Program {
    static void Main() {
        LineSegment L1 = new LineSegment();
        LineSegment L2 = new LineSegment(2, 3, 5, 7);
        LineSegment L3 = new LineSegment(L2); // Використання конструктора копіювання

        L3 = L3 * 2;  // Збільшення L3 у 2 рази
        L1 = L3 + L2; // Додавання L3 та L2

        // Вивід результатів
        Console.WriteLine("L1: ");
        L1.Display();
        Console.WriteLine("L2: ");
        L2.Display();
        Console.WriteLine("L3: ");
        L3.Display();
    }
}

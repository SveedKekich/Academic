using System;

class Program
{
    static void Main()
    {
        Console.Write("Введіть радіус вектора (r): ");
        double radius = Convert.ToDouble(Console.ReadLine());

        Console.Write("Введіть кут (в градусах): ");
        double angleDegrees = Convert.ToDouble(Console.ReadLine());
        double angleRadians = angleDegrees * Math.PI / 180; // Переведення в радіани

        VectorPolar vector = new VectorPolar(radius, angleRadians);
        vector.PrintInfo();

        var (x, y) = vector.GetCartesianCoordinates();
        Console.WriteLine($"Координати кінця вектора: (x = {x}, y = {y})");
    }
}
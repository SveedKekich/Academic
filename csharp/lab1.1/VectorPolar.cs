using System;

public class VectorPolar
{
    public double Radius { get; set; }
    public double Angle { get; set; } // в радіанах

    public VectorPolar(double radius, double angle)
    {
        Radius = radius;
        Angle = angle;
    }

    public void PrintInfo()
    {
        Console.WriteLine($"Вектор у полярних координатах: (r = {Radius}, θ = {Angle} рад)");
    }

    public (double x, double y) GetCartesianCoordinates()
    {
        double x = Radius * Math.Cos(Angle);
        double y = Radius * Math.Sin(Angle);
        return (x, y);
    }
}
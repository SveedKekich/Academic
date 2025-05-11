using System;

public class Expression
{
    private double a, b, c, d;

    public Expression(double a, double b, double c, double d)
    {
        this.a = a;
        this.b = b;
        this.c = c;
        this.d = d;
    }

    private double LogBase10(double value)
    {
        if (value <= 0)
            throw new ArgumentException("Logarithm of non-positive number.");
        return Math.Log10(value);
    }

    public double Calculate()
    {
        double numerator = LogBase10(4 * b - c) * a;
        double denominator = b + (c / d) - 1;

        if (denominator == 0)
            throw new DivideByZeroException("Division by zero in denominator.");

        return numerator / denominator;
    }

    public double A => a;
    public double B => b;
    public double C => c;
    public double D => d;
}

using System;

class Rectangle : Figure {
    private double x1, y1, x2, y2;

    public Rectangle(double x1, double y1, double x2, double y2) {
        this.x1 = x1;
        this.y1 = y1;
        this.x2 = x2;
        this.y2 = y2;
    }

    public override double Area() {
        return Math.Abs((x2 - x1) * (y2 - y1));
    }

    public override double Perimeter() {
        return 2 * (Math.Abs(x2 - x1) + Math.Abs(y2 - y1));
    }
}
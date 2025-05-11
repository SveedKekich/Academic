using System;

class Circle : Figure {
    private double radius;

    public Circle(double radius) {
        this.radius = radius;
    }

    public override double Area() {
        return Math.PI * radius * radius;
    }

    public override double Perimeter() {
        return 2 * Math.PI * radius;
    }
}
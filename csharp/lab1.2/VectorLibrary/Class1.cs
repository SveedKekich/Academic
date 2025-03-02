using System;

namespace VectorLibrary
{
    public class Vector
    {
        private double length;
        private double angle; // Кут у градусах

        // Конструктори
        public Vector()
        {
            length = 0;
            angle = 0;
        }

        public Vector(double len, double ang)
        {
            length = len;
            angle = ang;
        }

        public Vector(Vector other)
        {
            length = other.length;
            angle = other.angle;
        }

        // Властивості 
        public double Length => length;
        public double Angle => angle;

        // Метод обчислення координат кінця вектора
        public void GetEndCoordinates(out double x, out double y)
        {
            double rad = angle * Math.PI / 180.0;
            x = length * Math.Cos(rad);
            y = length * Math.Sin(rad);
        }
    }
}

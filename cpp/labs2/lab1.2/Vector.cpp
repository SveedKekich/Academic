#include "Vector.h"
#include <cmath>

// Конструктори
Vector::Vector() : length(0), angle(0) {}

Vector::Vector(double len, double ang) : length(len), angle(ang) {}

Vector::Vector(const Vector& other) : length(other.length), angle(other.angle) {}

// Гетери
double Vector::getLength() const {
    return length;
}

double Vector::getAngle() const {
    return angle;
}

// Метод обчислення координат кінця вектора
void Vector::getEndCoordinates(double& x, double& y) const {
    double rad = angle * M_PI / 180.0;
    x = length * cos(rad);
    y = length * sin(rad);
}

#include "Vector.h"
#include <cmath>

Vector::Vector(double r, double theta) : r(r), theta(theta) {}

void Vector::getCartesianCoordinates(double &x, double &y) const {
    double thetaRad = theta * M_PI / 180.0; // Перетворення градусів у радіани
    x = r * cos(thetaRad);
    y = r * sin(thetaRad);
}

void Vector::printVectorInfo() const {
    double x, y;
    getCartesianCoordinates(x, y);
    std::cout << "Полярні координати: R = " << r << ", Θ = " << theta << "°" << std::endl;
    std::cout << "Координати кінця вектора: X = " << x << ", Y = " << y << std::endl;
}
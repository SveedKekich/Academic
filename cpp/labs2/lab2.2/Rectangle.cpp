#include "Rectangle.h"
#include <cmath>

Rectangle::Rectangle(double x1, double y1, double x2, double y2) : x1(x1), y1(y1), x2(x2), y2(y2) {}

double Rectangle::area() const {
    return abs((x2 - x1) * (y2 - y1));
}

double Rectangle::perimeter() const {
    return 2 * (abs(x2 - x1) + abs(y2 - y1));
}
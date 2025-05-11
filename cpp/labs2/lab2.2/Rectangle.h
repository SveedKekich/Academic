#ifndef RECTANGLE_H
#define RECTANGLE_H
#include "Figure.h"

class Rectangle : public Figure {
private:
    double x1, y1, x2, y2;
public:
    Rectangle(double x1, double y1, double x2, double y2);
    double area() const override;
    double perimeter() const override;
};

#endif

#ifndef CIRCLE_H
#define CIRCLE_H
#include "Figure.h"

class Circle : public Figure {
private:
    double radius;
public:
    explicit Circle(double r);
    double area() const override;
    double perimeter() const override;
};

#endif
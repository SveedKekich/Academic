#ifndef FIGURE_H
#define FIGURE_H

class Figure {
public:
    virtual double area() const = 0;
    virtual double perimeter() const = 0;
    virtual ~Figure() = default;
};

#endif

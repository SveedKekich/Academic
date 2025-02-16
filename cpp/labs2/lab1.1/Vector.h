#ifndef VECTOR_H
#define VECTOR_H

#include <iostream>

class Vector {
private:
    double r; // Довжина вектора
    double theta; // Кут у градусах

public:
    Vector(double r, double theta);
    void getCartesianCoordinates(double &x, double &y) const;
    void printVectorInfo() const;
};

#endif // VECTOR_H

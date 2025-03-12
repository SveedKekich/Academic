#ifndef VECTOR_H
#define VECTOR_H

class Vector {
private:
    double length;
    double angle; // Кут у градусах

public:
    // Конструктори
    Vector();
    Vector(double len, double ang);
    Vector(const Vector& other);

    // Гетери
    double getLength() const;
    double getAngle() const;

    // Метод обчислення координат кінця вектора
    void getEndCoordinates(double& x, double& y) const;
};

#endif // VECTOR_H

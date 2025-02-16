#include <iostream>
#include "Vector.h"

int main() {
    double r, theta;

    std::cout << "Введіть довжину вектора (R): ";
    std::cin >> r;

    std::cout << "Введіть кут (Θ) у градусах: ";
    std::cin >> theta;

    Vector vector(r, theta);
    vector.printVectorInfo();

    return 0;
}
#include <iostream>
#include "Vector.h"

int main() {
    double length, angle;

    std::cout << "Enter lenght of a vector: ";
    std::cin >> length;

    std::cout << "Enter angle (in degrees): ";
    std::cin >> angle;

    Vector v(length, angle);

    double x, y;
    v.getEndCoordinates(x, y);

    std::cout << "Vector end coordinates: (" << x << ", " << y << ")" << std::endl;

    return 0;
}

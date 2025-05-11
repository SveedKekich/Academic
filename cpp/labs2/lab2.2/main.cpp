#include "Rectangle.h"
#include "Circle.h"
#include <iostream>
using namespace std;

void printFigureInfo(const Figure& fig) {
    cout << "Площа: " << fig.area() << ", Периметр: " << fig.perimeter() << endl;
}

int main() {
    Rectangle rect(0, 0, 4, 3);
    Circle circ(5);

    cout << "Прямокутник: ";
    printFigureInfo(rect);

    cout << "Коло: ";
    printFigureInfo(circ);

    return 0;
}

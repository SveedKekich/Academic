#include <iostream>
#include <cmath>

class LineSegment {
private:
    double x1, y1, x2, y2;

public:
    // Конструктор за замовчуванням
    LineSegment() : x1(0), y1(0), x2(1), y2(1) {}

    // Конструктор з параметрами
    LineSegment(double x1, double y1, double x2, double y2) 
        : x1(x1), y1(y1), x2(x2), y2(y2) {}

    // Конструктор копіювання
    LineSegment(const LineSegment& other) 
        : x1(other.x1), y1(other.y1), x2(other.x2), y2(other.y2) {}

    // Метод обчислення довжини відрізка
    double length() const {
        return sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
    }

    // Перевантаження оператора множення (масштабування відрізка)
    LineSegment operator*(double factor) const {
        return LineSegment(x1, y1, x1 + (x2 - x1) * factor, y1 + (y2 - y1) * factor);
    }

    // Перевантаження оператора додавання
    LineSegment operator+(const LineSegment& other) const {
        return LineSegment(x1, y1, other.x2, other.y2);
    }

    // Виведення інформації про відрізок
    void display() const {
        std::cout << "LineSegment((" << x1 << ", " << y1 << ") -> ("
                  << x2 << ", " << y2 << ")), Length: " << length() << std::endl;
    }
};

int main() {
    LineSegment L1, L2(2, 3, 5, 7), L3 = L2;  // Використання різних конструкторів
    L3 = L3 * 2;  // Збільшення L3 у 2 рази
    L1 = L3 + L2; // Додавання L3 та L2

    // Вивід результатів
    std::cout << "L1: ";
    L1.display();
    std::cout << "L2: ";
    L2.display();
    std::cout << "L3: ";
    L3.display();

    return 0;
}

#include "Expression.h"
#include <cmath>

Expression::Expression(double a, double b, double c, double d)
    : a(a), b(b), c(c), d(d) {}

double Expression::LogBase10(double value) const {
    if (value <= 0)
        throw std::invalid_argument("Logarithm of non-positive number.");
    return std::log10(value);
}

double Expression::Calculate() const {
    double numerator = LogBase10(4 * b - c) * a;
    double denominator = b + (c / d) - 1;

    if (denominator == 0)
        throw std::runtime_error("Division by zero in denominator.");

    return numerator / denominator;
}

double Expression::GetA() const { return a; }
double Expression::GetB() const { return b; }
double Expression::GetC() const { return c; }
double Expression::GetD() const { return d; }

#pragma once
#include <stdexcept>

class Expression {
private:
    double a, b, c, d;
    double LogBase10(double value) const;

public:
    Expression(double a, double b, double c, double d);

    double Calculate() const;
    
    double GetA() const;
    double GetB() const;
    double GetC() const;
    double GetD() const;
};

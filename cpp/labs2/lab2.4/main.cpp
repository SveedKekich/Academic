#include <iostream>
#include <vector>
#include "Expression.h"

int main() {
    std::vector<Expression> expressions = {
        Expression(2, 3, 5, 1),
        Expression(1, 1, 4, 2),
        Expression(1, 2, 8, 0.5)  // приклад з потенційною помилкою
    };

    for (size_t i = 0; i < expressions.size(); ++i) {
        try {
            double result = expressions[i].Calculate();
            std::cout << "Expression " << i + 1 << " result: " << result << "\n";
        } catch (const std::exception& ex) {
            std::cout << "Error in expression " << i + 1 << ": " << ex.what() << "\n";
        }
    }

    return 0;
}

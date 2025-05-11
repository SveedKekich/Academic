#include <iostream>
#include "Text.h"

int main() {
    Text text;
    text.AddLine(TextLine("Hello"));
    text.AddLine(TextLine("world"));
    text.AddLine(TextLine("C++"));
    
    text.ToUpperAll();
    std::cout << "Text after ToUpper:\n";
    for (const auto& line : text.GetLines()) {
        std::cout << line.GetContent() << std::endl;
    }

    std::cout << "Found 'WORLD': " << text.FindLine("WORLD") << std::endl;

    text.RemoveLinesOfLength(5);
    std::cout << "Text after removing length 5:\n";
    for (const auto& line : text.GetLines()) {
        std::cout << line.GetContent() << std::endl;
    }

    return 0;
}

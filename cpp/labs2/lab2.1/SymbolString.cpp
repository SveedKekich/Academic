#include "SymbolString.h"
#include <iostream>

SymbolString::SymbolString(const string& str, char oldChar, char newChar) : BaseString(str) {
    replaceChar(oldChar, newChar);
}

void SymbolString::replaceChar(char oldChar, char newChar) {
    for (char& c : value) {
        if (c == oldChar) c = newChar;
    }
}

void SymbolString::print() const {
    cout << "Рядок: " << value << "\n";
}
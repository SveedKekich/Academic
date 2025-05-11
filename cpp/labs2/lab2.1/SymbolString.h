#ifndef SYMBOLSTRING_H
#define SYMBOLSTRING_H

#include "BaseString.h"

class SymbolString : public BaseString {
public:
    SymbolString(const string& str, char oldChar, char newChar);
    void replaceChar(char oldChar, char newChar);
    void print() const;
};

#endif


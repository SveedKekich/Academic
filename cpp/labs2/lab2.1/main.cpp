#include "SymbolString.h"
#include <iostream>
#include <cstring>
using namespace std;

int main() {
    SymbolString s("hello world", 'o', 'a');
    s.print();
    cout << "Довжина: " << s.getLength() << endl;
    return 0;
}

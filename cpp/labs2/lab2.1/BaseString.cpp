#include "BaseString.h"

BaseString::BaseString() : value("") {}

BaseString::BaseString(const string& str) : value(str) {}

int BaseString::getLength() const {
    return value.length();
}

string BaseString::getValue() const {
    return value;
}
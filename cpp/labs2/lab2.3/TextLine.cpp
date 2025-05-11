#include "TextLine.h"
#include <algorithm>

TextLine::TextLine(const std::string& text) : content(text) {}

std::string TextLine::GetContent() const {
    return content;
}

void TextLine::ToUpper() {
    std::transform(content.begin(), content.end(), content.begin(), ::toupper);
}

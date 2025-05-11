#include "Text.h"
#include <algorithm>

void Text::AddLine(const TextLine& line) {
    lines.push_back(line);
}

void Text::RemoveLine(int index) {
    if (index >= 0 && index < static_cast<int>(lines.size()))
        lines.erase(lines.begin() + index);
}

void Text::Clear() {
    lines.clear();
}

void Text::ToUpperAll() {
    for (auto& line : lines)
        line.ToUpper();
}

int Text::FindLine(const std::string& lineText) const {
    int count = 0;
    for (const auto& line : lines)
        if (line.GetContent() == lineText)
            ++count;
    return count;
}

void Text::RemoveLinesOfLength(size_t length) {
    lines.erase(std::remove_if(lines.begin(), lines.end(),
        [length](const TextLine& line) {
            return line.GetContent().size() == length;
        }), lines.end());
}

const std::vector<TextLine>& Text::GetLines() const {
    return lines;
}

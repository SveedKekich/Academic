#pragma once
#include <vector>
#include "TextLine.h"

class Text {
private:
    std::vector<TextLine> lines;
public:
    void AddLine(const TextLine& line);
    void RemoveLine(int index);
    void Clear();
    void ToUpperAll();
    int FindLine(const std::string& lineText) const;
    void RemoveLinesOfLength(size_t length);
    const std::vector<TextLine>& GetLines() const;
};

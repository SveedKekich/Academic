#pragma once
#include <string>
#include "IRegister.h"

class TextLine : public IRegister {
private:
    std::string content;
public:
    TextLine(const std::string& text);
    std::string GetContent() const;
    void ToUpper() override;
};

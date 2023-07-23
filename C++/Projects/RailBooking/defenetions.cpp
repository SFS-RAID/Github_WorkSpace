#include <iostream>
#include "defenitions.h"

constexpr unsigned int str2int(const char* str, int h) {
    return !str[h] ? 5381 : (str2int(str, h + 1) * 33) ^ str[h];
}

std::string input(const std::string& text) {
    std::string var;
    std::cout << text;
    std::cin >> var;
    return var;
}

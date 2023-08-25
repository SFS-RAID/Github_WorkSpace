#include <iostream>
#include <stdio.h>
#include <string>
#include "classes.cpp"
using namespace std;


constexpr unsigned int str2int(const char* str, int h = 0)
{
    return !str[h] ? 5381 : (str2int(str, h+1) * 33) ^ str[h];
}

station chennai("chennai", "SR", 8, 4, 16, 12);
station vijayawada("vijayawada", "SCR", 16, 4, 4, 8);

route mas_to_bza(chennai, vijayawada, 450);

train pinakini(12711, "Pinakini Express", mas_to_bza, 0.25);


string input(string text){
    string var;
    cout << text;
    cin >> var;
    return var;
}

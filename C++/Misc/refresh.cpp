#include <iostream>
#include <stdio.h>
using std::cout, std::cin;

class aclass{
    public:
        int g = 100;
        int viewpg(){
            return pg;
        }
    private:
        int pg = 500;
};


int main(){
    cout << "Start";
    aclass sc;
    cout << sc.viewpg();
}
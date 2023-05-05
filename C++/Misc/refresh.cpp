#include <iostream>
#include <stdio.h>
using std::cout, std::cin;

class aclass{
    public:
        aclass(int sg){
            this->pg = sg;
        }
        int g = 100;
        std::string name = "plane";
        int viewpg(){
            return pg;
        }
    private:
        int pg = 500;
};


int main(){
    cout << "Start\n";
    aclass sc(55);
    cout << sc.viewpg() << "\n";
    cout << sc.name << "\n";
}
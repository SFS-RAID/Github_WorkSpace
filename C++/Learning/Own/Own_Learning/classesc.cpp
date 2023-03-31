#include <iostream>
using namespace std;

class aClass{
    public:
        int x;
        void MyFunction(){
            cout << "Hello World\n";
        }
};

int main(){
    aClass* obj = new aClass();
    obj->MyFunction();
    delete obj;
    int x = 10;
    cout << x << endl;
    return 0;
}
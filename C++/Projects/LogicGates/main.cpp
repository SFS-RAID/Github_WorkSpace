#include <iostream>
#include <string>
#include <vector>
using namespace std;

class gate
{
private:
    /* data */
public:
    vector<bool> input, output;
    gate(size_t inputsize, size_t outputsize){
        input.resize(inputsize);
        output.resize(outputsize);
    };
    ~gate(){};
};



int main(int argc, char const *argv[])
{
    cout << "Start!";
    return 0;
}

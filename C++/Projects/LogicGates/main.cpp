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
    cout << "Start!" << endl;
    gate andgate(2, 1);
    andgate.input[7] = 1;
    cout << andgate.input.size() << endl;
    return 0;
}

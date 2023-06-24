#include <string>
using namespace std;

class station
{
private:
    /* data */
public:
    string name;
    station(string name){
        this->name = name;
    }
};


class train
{
private:
    /* data */
public:
    int train_num;
    string name, source, destination;
    train(int train_no, string train_name, station& start, station& end){
        this->train_num=train_no;
        this->name = train_name;
        this->source = start.name;
        this->destination = end.name;
    }
};
#include <string>
using namespace std;

class station
{
private:
    /* data */
public:
    string name;
    string division="";

    station(string name, string div="NA")
        : name(name), division(div)
        /*Initalising, outvariable(parameter)=
        this->outvariable = parameter*/
    {
    }
};

station defaultstn("default");
station defaultstn2("default2");

class route{
public:
    station& start;
    station& end;
    //Declare station variable for object
    int distance;

    route(station& startpoint, station& endpoint, int distance=100)
        : start(startpoint), end(endpoint), distance(distance)
    {
    }
};

route defaultroute(defaultstn, defaultstn2);

class train
{
private:
    /* data */
public:
    int train_num, distance=0;
    string name;
    route& route_train;

    train(int train_no, string train_name, route& trainroute)
        : train_num(train_no), name(train_name), route_train(trainroute)
    {
        distance = route_train.distance;
    }
};
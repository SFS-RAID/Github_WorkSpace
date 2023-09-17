#include <string>
#include <cmath>
using namespace std;

class station
{
private:
    /* data */
public:
    string name;
    string division="";
    int livetr_near, livetr_far;
    
    int yard_tracks, platforms;

    station(string name, string div="NA", int livetracks_near=2, int livetracks_far=2,
    int yardtracks=0, int platform_count=4)
        : name(name), division(div), livetr_near(livetracks_near),
         livetr_far(livetracks_near), yard_tracks(yardtracks), platforms(platform_count)
        /*Initalising, outvariable(parameter)=
        this->outvariable = parameter*/
    {
    }
};

station defaultstn("default");
station defaultstn2("default2");

class route{
public:
    station& start, end;
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
    int train_num, distance=0, cost;
    string name;
    route& route_train;

    train(int train_no, string train_name, route& trainroute, int cost_perkm)
        : train_num(train_no), name(train_name), route_train(trainroute)
    {
        distance = route_train.distance;
        cost = round(distance * cost_perkm);
    }
};
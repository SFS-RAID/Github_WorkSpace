#ifndef CLASSES_H
#define CLASSES_H

#include <string>

class Station {
public:
    std::string name;
    std::string division;
    int livetr_near, livetr_far;
    int yard_tracks, platforms;

    Station(const std::string& name, const std::string& div = "NA", int livetracks_near = 2,
            int livetracks_far = 2, int yardtracks = 0, int platform_count = 4);
};

extern Station defaultstn;
extern Station defaultstn2;

class Route {
public:
    Station& start, end;
    int distance;

    Route(Station& startpoint, Station& endpoint, int distance = 100);
};

extern Route defaultroute;

class Train {
public:
    int train_num, distance = 0, cost;
    std::string name;
    Route& route_train;

    Train(int train_no, const std::string& train_name, Route& trainroute, int cost_perkm);
};

#endif // CLASSES_H
 

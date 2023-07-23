#include "classes.h"
#include <cmath>

Station::Station(const std::string& name, const std::string& div, int livetracks_near,
    int livetracks_far, int yardtracks, int platform_count)
    : name(name), division(div), livetr_near(livetracks_near),
    livetr_far(livetracks_near), yard_tracks(yardtracks), platforms(platform_count) {
}

Station defaultstn("default");
Station defaultstn2("default2");

Route::Route(Station& startpoint, Station& endpoint, int distance)
    : start(startpoint), end(endpoint), distance(distance) {
}

Route defaultroute(defaultstn, defaultstn2);

Train::Train(int train_no, const std::string& train_name, Route& trainroute, int cost_perkm)
    : train_num(train_no), name(train_name), route_train(trainroute) {
    distance = route_train.distance;
    cost = round(distance * cost_perkm);
}

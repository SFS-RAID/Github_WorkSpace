#ifndef RAID_UTILS_H
#define RAID_UTILS_H

#include <iostream>
#include <vector>
#include <random>
#include <string>

#define LINE "\n"
#define SPACE " "

using namespace std;

int randomint(int min, int max) {
    random_device rd;
    mt19937 mt(rd());
    uniform_int_distribution<int> dist(min, max);
    return dist(mt);
}

double randomdouble(double min, double max) {
    random_device rd;
    mt19937 mt(rd());
    uniform_real_distribution<double> dist(min, max);
    return dist(mt);
}

bool randbool() {
    return randomint(0, 1) ? true : false;
}

template<typename T, size_t N>
T randarray(const T (&arr)[N]) {
    return arr[randomint(0, N - 1)];
}

template<typename T>
T randvector(const vector<T>& vec) {
    return vec[randomint(0, vec.size() - 1)];
}

template<typename T>
string to_string(const T& value) {
    return std::to_string(value);
}
string to_string(const string& value) {
    return value;
}
string to_string(const char* value) {
    return value;
}

template<typename T>
string concatenate_strings(const T& first) {
    return to_string(first);
}
template<typename T, typename... Args>
string concatenate_strings(const T& first, const Args&... args) {
    return to_string(first) + concatenate_strings(args...);
}

template<typename... Args>
void print(const Args&... args) {
    cout << concatenate_strings(args...) << LINE;
}

template<typename T>
void println(T msg, int newlines = 0) {
    string newlinechar = "";
    for (int i = 0; i < newlines + 1; ++i) {
        newlinechar += LINE;
    }
    cout << msg << newlinechar;
}

#endif // RAID_UTILS_H

#include <iostream>
#include <string>

using namespace std;

int main()
{
    string name;
    int age;
    string fname = "Shaik";

    cout << "\nType your age: ";
    cin >> age;
    cin.ignore();
    
    cout << "Your age is " << age << endl;
    cout << "Type your name: ";
    getline(cin, name);
    cout << "Your name is " << fname + " something " + name << endl;
}
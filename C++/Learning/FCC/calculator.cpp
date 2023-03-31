#include <iostream>
#include <string>
using namespace std;

int main (){
    double num1;
    double num2;
    char op;

    cout << "HI" << endl;
    cout << "Type a number: ";
    cin >> num1;
    cin.ignore();
    cout << "\nType another number: ";
    cin >> num2;
    cin.ignore();
    cout << "\nType a operator: ";
    cin >> op;

    switch (op){
    case '+':
        cout << num1 << " + " << num2 << " = " <<  num1 + num2;
        break;
    case '-':
        cout << num1 << " - " << num2 << " = " <<  num1 - num2;
        break;
    case '*':
        cout << num1 << " * " << num2 << " = " <<  num1 * num2;
        break;
    case '/':
        cout << num1 << "/" << num2 << " = " <<  num1 / num2;
        break;
    default:
        cout << "Unknown operator";
        break;
    }
}
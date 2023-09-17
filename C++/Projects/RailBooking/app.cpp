#include <iostream>
#include <stdio.h>
#include <string>
#include "classes.cpp"
#include "defenitions.cpp"
using namespace std;


int main(){
	cout << "program ran\n";
	string UserName = "User";
	cout << "Hello " << UserName << "\n\n";

	string command;

	while (command != "exit")
	{
	cout << "\nType a command: ";
	cin >> command;
	switch (str2int(command.c_str()))
	{
	case /* constant-expression */str2int("help"):
		/* code */
		printf("Here is the list of commands\n\n");
		printf("help: display help");
		break;
	
	case str2int("exit"):
	    printf("Program successfully exit");
	    break;
	
	case str2int("test"):
	    printf(input("what is your name").c_str());


	default:
	    printf("Invalid Command\nType help for Commands");
		break;
	}
	printf("\n");
	}
}
#include <iostream>
#include "defenitions.h"
#include "classes.h"

int main() {
    std::cout << "Program ran\n";
    std::string userName = "User";
    std::cout << "Hello " << userName << "\n\n";

    std::string command;

    while (command != "exit") {
        std::cout << "\nType a command: ";
        std::cin >> command;

        switch (str2int(command.c_str())) {
            case str2int("help"):
                std::cout << "Here is the list of commands\n\n";
                std::cout << "help: display help";
                break;
            case str2int("exit"):
                std::cout << "Program successfully exits";
                break;
            case str2int("test"):
                std::cout << input("What is your name: ");
                break;
            default:
                std::cout << "Invalid Command\nType help for Commands";
                break;
        }

        std::cout << "\n";
    }

    return 0;
}

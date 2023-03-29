#include <iostream>
#include <cstdlib>
#include <ctime>

class Dice {
public:
    std::pair<int, int> roll() {
        srand(time(NULL));
        int num1 = rand() % 6 + 1;
        int num2 = rand() % 6 + 1;
        return std::make_pair(num1, num2);
    }
};

int main() {
    Dice dice1;
    char roll_again;
    do {
        std::pair<int, int> roll = dice1.roll();
        std::cout << roll.first << ", " << roll.second << std::endl;
        std::cout << "Roll again? (y/n) : ";
        std::cin >> roll_again;
        while(roll_again != 'y' && roll_again != 'Y' && roll_again != 'n' && roll_again != 'N') {
          std::cout << "Invalid input, please enter 'y' or 'n': ";
          std::cin >> roll_again;
        }
    } while (roll_again == 'y' || roll_again == 'Y');

    return 0;
}

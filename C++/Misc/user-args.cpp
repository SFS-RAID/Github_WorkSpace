#include <iostream>
#include <cstring>
#include <stdio.h>
using namespace std;

int main(int argc, char** argv){
    printf("Hello\n");
    if (strcmp(argv[1], "action")==0){
        printf("The action is done\n");
    }
}
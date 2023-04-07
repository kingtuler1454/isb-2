#include <iostream>
#include <time.h>
#include <random>
#include <vector>
#include <fstream>
void main() {
    int result[127];
    int seed = 5;
    srand(time(0));
    for (int i = 0; i < 128; ++i) {
        seed = (rand() * rand() * seed + rand()) % 2;
        result[i] = seed;
    }
    std::ofstream out;         
    out.open("128.txt");      
    if (out.is_open())
    {
        for (int i = 0; i < 128; i++) out << result[i];
    }
    out.close();

}
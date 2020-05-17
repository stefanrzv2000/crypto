#include <iostream>
#include <fstream>

using namespace std;

ifstream fin("frecs.txt");

int main(){
    char c;
    long long int f;
    for(int i = 0; i < 26; i++){
        fin >> c;
        fin >> f;
        printf("frecs[%d] = %lld;\n",c-'A',f);
    }
    return 0;
}
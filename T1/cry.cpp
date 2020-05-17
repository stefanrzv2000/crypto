#include <iostream>
#include <string>
#include <stdio.h>

using namespace std;

char toLetter(int n){
    return 'A' + n%26;
}

int toInt(char c){
    if(c >= 'A' && c <= 'Z'){
        return c - 'A';
    }
    return -1;
}

string toUp(string text){
    string rez = "";
    for (auto c : text){
        char cc = c;
        if(c>= 'a' && c <= 'z'){
            cc = c - 32;
        }
        rez += cc;
    }
    return rez;
}

string getLetters(string text){
    string rez = "";
    for (auto c:text){
        if(c >= 'A' && c <= 'Z'){
            rez += c;
        }
    }
    rez+="\0";
    return rez;
}

void readFile(string& text, FILE* f){
    text = "";
    char c;
    while(!feof(f)){
        fscanf(f,"%c",&c);
        if(c>= 'a' && c <= 'z'){
            c = c - 32;
        }
        if(c >= 'A' && c <= 'Z'){
            text += c;
        }
    }
}

string crypt(string text, string key){
    int m = key.size();
    string rez = "";
    int i = 0;
    for(auto c: text){
        rez += toLetter((toInt(c) + toInt(key[i]))%26);
        i = (i+1)%m;
    }
    return rez;
}

float IC(string text){
    int frec[30] = {0};
    for(auto c: text){
        frec[toInt(c)]++;
    }
    int s = 0;
    int a = 0;
    for(int i = 0; i < 26; i++){
        a+=frec[i];
        s+=(frec[i]*(frec[i]-1));
    }
    return float(s)/a/(a-1);
}

string filter(string text, int len, int poz){
    string rez = "";
    int index = poz;
    int ll = text.size();
    while(index < ll){
        rez += text[index];
        index += len;
    }
    return rez;
}

string randomKey(int len){
    string rez = "";
    for(int i = 0; i < len; i++){
        rez += toLetter(rand());
    }
    return rez;
}

int main(int argc, char* argv[]){
    srand(time(NULL));
    string filename;
    if(!argc) {
        printf("Introduceti numele fisierului de prelucrat: ");
        cin >> filename;
    }
    else{
        filename = argv[1];
    }
    FILE* f = fopen(filename.c_str(),"r");
    string text;
    readFile(text,f);
    //string plain_text = getLetters(toUp(text));
    //cout << text << "\n";
    cout << IC(text) << "\n";
    string key;
    printf("Introduceti cheia de criptare (#<lenght> pentru o cheie random): ");
    cin >> key;
    if(key[0] == '#'){
        int len = atoi(key.c_str()+1);
        printf("len = %d\n", len);
        key = randomKey(len);
        printf("key = %s\n", key.c_str());
    }
    else{    key = getLetters(toUp(key)); }
    string crypto_text = crypt(text,key);
    //cout << "\n\n" << crypto_text << "\n";
    FILE* fo = fopen(argv[2],"w+");
    fprintf(fo,"%s\n",crypto_text.c_str());
}
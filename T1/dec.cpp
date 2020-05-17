#include <iostream>
#include <string>
#include <stdio.h>

using namespace std;

typedef long double ld;

#define LMAX 1000
#define WITHMIC 1

FILE* fout = fopen("dec.out","w+");

ld frecs[30];
ld sum = 0;

void initfrecs(){
    frecs[4] = 529117365;
    frecs[19] = 390965105;
    frecs[0] = 374061888;
    frecs[14] = 326627740;
    frecs[8] = 320410057;
    frecs[13] = 313720540;
    frecs[18] = 294300210;
    frecs[17] = 277000841;
    frecs[7] = 216768975;
    frecs[11] = 183996130;
    frecs[3] = 169330528;
    frecs[2] = 138416451;
    frecs[20] = 117295780;
    frecs[12] = 110504544;
    frecs[5] = 95422055;
    frecs[6] = 91258980;
    frecs[15] = 90376747;
    frecs[22] = 79843664;
    frecs[24] = 75294515;
    frecs[1] = 70195826;
    frecs[21] = 46337161;
    frecs[10] = 35373464;
    frecs[9] = 9613410;
    frecs[23] = 8369915;
    frecs[25] = 4975847;
    frecs[16] = 4550166;

    ld sum = 0;
    for(int i = 0; i < 26; i++){
        sum += frecs[i];
    }
    for(int i = 0; i < 26; i++){
        frecs[i] = frecs[i]/sum;
    }
}

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

ld IC(string text){
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
    return ld(s)/a/(a-1);
}

ld MIC(string text){
    int frec[30] = {0};
    for(auto c: text){
        frec[toInt(c)]++;
    }
    int s = 0;
    int a = 0;
    for(int i = 0; i < 26; i++){
        a+=frec[i];
        s+=(frecs[i]*frec[i]);
    }
    return ld(s)/a;
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

int cond(ld x){
    return (x>0.062)&&(x<0.1);
}

ld ICS[LMAX][LMAX];

string decode(string text, string key){
    int m = key.size();
    string rez = "";
    int i = 0;
    for(auto c: text){
        rez += toLetter((26 + toInt(c) - toInt(key[i]))%26);
        i = (i+1)%m;
    }
    return rez;
}

int main(int argc, char* argv[]){
    initfrecs();
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
    int len;
    for(len = 2; len < 100; len++){
        int ok = 1;
        for(int i = 0; i < len; i ++){
            ICS[len][i] = IC(filter(text,len,i));
            //if(!(len%100))printf("%LF ",ICS[len][i]);
            if(!cond(ICS[len][i])) ok=0;
            //else ok -= 3;
        }
        if(ok) {printf("m = %d\n",len);break;}
    }

    for(; len < LMAX; len++){
        //if(!(len%100))printf("%d: ",len);
        int ok = 0;
        for(int i = 0; i < len; i++){
            ICS[len][i] = IC(filter(text,len,i));
            //if(!(len%100))printf("%LF ",ICS[len][i]);
            if(cond(ICS[len][i])) ok+=2;
            else ok -= 3;
        }
        //printf("len = %d: ok = %d\n",len,ok);
        //if(!(len%100))printf("\n");
        if(ok >= 0) {printf("m = %d\n",len);break;}
    }
    cout << "len = " << len << "\n";
    string key = "";
    for(int i = 0; i < len; i++){
        //printf("i: %d\n",i);
        string ttt = filter(text,len,i);
        int frec[30] = {0};
        for(auto c: ttt){
            frec[toInt(c)]++;
        }
        char letter;
        
        if(WITHMIC){
            int a = 0;
            for(int i = 0; i < 26; i++){
                //printf("%c - frec: %d\n",char('A'+i),frec[i]);
                a+=frec[i];
            }
            ld mic;
            ld micMax = 0;
            for(int s = 0; s < 26; s++){
                mic = 0;
                for(int j = 0; j < 26; j++){
                    mic += frecs[j]*frec[(j+s)%26];
                }
                mic = mic/a;
                //printf("\t%c: %Lf\n",'A'+s,mic);
                if(mic > micMax){
                    letter = 'A' + s;
                    micMax = mic;
                }
            }
        }
        else{
            int fmax = 0;
            char se = 0;
            for(int i = 0; i < 26; i++){
                if(frec[i]>fmax){
                    fmax = frec[i];
                    se = 'A' + i;
                }
            }
            letter = toLetter(se - 'E' + 26);
        }

        key += letter;
    }
    cout << "key : " + key + "\n";
    fprintf(fout,"%s\n",decode(text,key).c_str());
}
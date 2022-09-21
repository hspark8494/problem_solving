#include <iostream>
#include <math.h>
using namespace std;

int main(){
    int S, A;
    double B;
    cin >> S;
    cin >> A;
    cin >> B;
    int val = ceil((S-A) / B);
    int result = 0;
    if(val>=0){
        result = 250 + val * 100;
    }else if(S!=0){
        result = 250;
    }
    cout << result;
    
    return 0;
}
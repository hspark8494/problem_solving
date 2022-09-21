#include <iostream>

using namespace std;

int main(){
    int a;
    cin >> a;
    double b = 100-a;
    cout.precision(15);
    printf("%.12lf \n", 1+b/a);
    printf("%.12lf \n", 1+a/b);
    return 0;
}
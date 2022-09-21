#include <iostream>
using namespace std;

int main()
{
    int a, b, c;
    int d, e, f;
    scanf("%d %d %d", &a, &b, &c);
    scanf("%d %d %d", &d, &e, &f);
    printf("%d", max(d - a, 0) + max(e - b, 0) + max(f - c, 0));
    return 0;
}
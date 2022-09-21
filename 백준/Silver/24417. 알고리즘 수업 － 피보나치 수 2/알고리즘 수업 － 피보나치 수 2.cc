#include <iostream>

using namespace std;

int main()
{
    int r;
    scanf("%d", &r);
    long result = 0;
    long a = 1;
    long b = 1;
    if (r == 0)
    {
        return 0;
    }
    else if (r == 1)
    {
        return 1;
    }
    for (int i = 2; i < r; i++)
    {
        long t = a;
        a = b;
        b = (t + b) % 1000000007;
    }
    printf("%d %d", b, r - 2);
    return 0;
}

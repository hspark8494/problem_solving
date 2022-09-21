#include <stdio.h>

int main()
{
    int b = 0;
    scanf("%d", &b);
    int p = 5 * b - 400;
    int result = 0;
    if (p < 100)
    {
        result = 1;
    }
    else if (p > 100)
    {
        result = -1;
    }
    printf("%d\n%d\n", p, result);
    return 0;
}
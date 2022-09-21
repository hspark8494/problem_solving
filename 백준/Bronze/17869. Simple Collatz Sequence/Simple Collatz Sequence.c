#include <stdio.h>

int main()
{
    long l = 0L;
    scanf("%ld", &l);
    int cnt = 0;
    while (l != 1L)
    {
        if (l % 2L == 0L)
        {
            l = l / 2L;
        }
        else
        {
            l++;
        }
        cnt++;
    }
    printf("%d\n", cnt);

    return 0;
}
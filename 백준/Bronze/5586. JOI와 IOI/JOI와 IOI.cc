#include <iostream>

using namespace std;

int main()
{
    string line;
    cin >> line;
    int ioi=0, joi=0;

    for (int i = 1; i < line.length()-1; i++)
    {
        if (line.at(i) == 'O' && line.at(i+1) == 'I'){
            if (line.at(i-1) == 'I'){
                ioi++;
            }else if(line.at(i-1) == 'J'){
                joi++;
            }
        }
    }
    printf("%d\n%d\n", joi, ioi);
    return 0;
}

#include <iostream>

using namespace std;

int main()
{
    string line;

    while (getline(cin, line))
    {
        int up = 0, low = 0, nums = 0, ws = 0;

        for (int i = 0; i < line.length(); i++)
        {
            char c = line.at(i);
            if (c >= 'a'){
                low++;
            }
            else if (c >= 'A'){
                up++;
            }
            else if (c >= '0'){
                nums++;
            }
            else{
                ws++;
            }
        }
        printf("%d %d %d %d\n", low, up, nums, ws);
    }
    return 0;
}

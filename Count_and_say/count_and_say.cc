#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n = 2;
    string str = to_string(1);
    for(int i = 0; i < n - 1; ++i)
    {
        int len = str.size();
        int k = 1;
        string res = "";
        for(int j = 0; j < len; ++j)
        {
            if(j != len - 1 && str[j] == str[j+1])
            {
                ++k;
            }
            else
            {
                res += to_string(k);
                res += str[j];
                k = 1;
            }
        }
        str = res;
    }
    cout << str;
    return 0;
}

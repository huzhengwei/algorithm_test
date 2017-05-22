#include <bits/stdc++.h>
using namespace std;
int main()
{
    string s = "Let's take Leetcode contest";
    auto iter1 = s.begin();
    auto iter2 = s.begin();
    while(iter2 != s.end())
    {
        auto iter = iter1;
        for(; iter != s.end(); ++iter)
        {
            if(!isblank(*iter))
            {
                break;
            }
        }
        iter1 = iter;
        for(iter = iter1; iter != s.end(); ++iter)
        {
            if(isblank(*iter))
            {
                break;
            }
        }
        iter2 = iter;
        reverse(iter1, iter2);
        if(iter2 == s.end()) break;
        iter1 = iter2 = ++iter;
    }
    cout << s;
    return 0;
}

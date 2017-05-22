#include <bits/stdc++.h>
using namespace std;
int main()
{
    string word = "FlaG";
    if(word.size() < 2) return true;
    if(word[0] >= 'a' && word[1] < 'a')
        return false;
    for(auto i = 2; i < word.size(); ++i)
    {
        if((word[i] >= 'a') != (word[i-1] >= 'a'))
            return false;
    }
    return true;
}

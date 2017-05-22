#include <bits/stdc++.h>
using namespace std;
int main()
{
    string ransomNote = "a";
    string magazine = "b";
    int map[26] = {0};
    for(auto c : magazine)
    {
        ++map[c - 'a'];
    }
    for(auto c : ransomNote)
    {
        if( --map[c - 'a'] < 0)
            return false;
    }
    return true;
}

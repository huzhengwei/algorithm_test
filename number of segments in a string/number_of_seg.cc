#include <bits/stdc++.h>
using namespace std;
int main()
{
    string s = "Hello, my name is John";
    istringstream ss(s);
    int i = 0;
    for(string w; ss >> w; ++i)
        ;
    cout << i;
    return 0;
}

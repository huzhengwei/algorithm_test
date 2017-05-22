#include<bits/stdc++.h>
using namespace std;
int main()
{
    string s = "abcdefg";
    int k = 2;
    for(int i = 0; (i + k)<= s.size(); i += 2*k)
    {
        string tmp = s.substr(i, k);
        std::reverse(tmp.begin(), tmp.end());
        s.replace(i, k, tmp);
    }
    cout << s << endl;
    return 0;
}

#include <bits/stdc++.h>
using namespace std;
int main()
{
    string a = "11";
    string b = "1;
    auto itera = a.rbegin();
    auto iterb = b.rbegin();
    string c = "";
    int ia, ib, pre, ic;
    while(itera != a.rend() || iterb != b.rend())
    {
        if(itera != a.rend())
        {
            ia = *itera - '0';
            ++itera;
        }
        else ia = 0;
        if(iterb != b.rend())
        {
            ib = *iterb - '0';
            ++iterb;
        }
        else ib = 0;
        ic = ia + ib + pre;
        c.append(1, '0' + ic % 2);
        pre = ic / 2;
    }
    if(pre) c.append(1, '1');
    reverse(c.begin(), c.end());
    cout << c ;
    return 0;
}

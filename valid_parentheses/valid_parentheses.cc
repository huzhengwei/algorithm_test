#include <bits/stdc++.h>
using namespace std;
bool isMatch(const string& s, int ls, int rs)
{
    switch(s[ls])
    {
        case '(':
            if(s[rs] == ')') return true;
            break;
        case '[':
            if(s[rs] == ']') return true;
            break;
        case '{':
            if(s[rs] == '}') return true;
            break;
        default:
            return false;
    }
    return false;
}
bool isRight(char c)
{
    if(c == ')' || c == ']' || c == '}')
        return true;
    return false;
}
int main()
{
    string s = "[(({})}]";
    int len = s.size();
    if(len % 2) return false;
    stack<int> stk;
    for(int i = 0; i < len; ++i)
    {
        if(stk.empty() || !isMatch(s, stk.top(), i))
        {
            if(isRight(s[i]))
                return false;
            else
                stk.push(i);

        }
        else
            stk.pop();
    }
    if(stk.empty())
        return true;
    return false;
}

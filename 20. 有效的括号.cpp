#include<iostream>
#include<stack>
#include<string>
using namespace std;

bool isValid(string strs) {
    if (strs.size() %2 != 0) return false;
    stack<char> container;
    for(auto tt:strs){
        char s = tt;
        if(s == '{' || s== '(' || s == '[')
        {
            cout<<"push"<<s<<endl;
            container.push(s);
        }
        else if (container.size() > 0)
        {
            if(s == ')')
            {
                if( container.top() == '(')
                    container.pop();
                else
                    return false;
            }
            else if( s== '}')
            {
                if( container.top() == '{')
                    container.pop();
                else
                    return false;
            }
            else if(s == ']')
            {
                if( container.top() == '[')
                    container.pop();
                else
                    return false;
            }
            }
            else return false;
        
    }
    if(container.size() == 0)
        return true;
    else return false;
}

int main()
{
string strs = "{}))";
    bool t = isValid(strs);
    cout<<t<<endl;
}
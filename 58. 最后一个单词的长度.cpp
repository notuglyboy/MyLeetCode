#include <iostream>
#include <vector>
using namespace std;

int lengthOfLastWord(string s) {
    int last_num = 0;
    int tmp = 0;
    for(auto i:s)
    {
        if(i == ' ')
        {
            if(tmp != 0)
                last_num = tmp;
            tmp = 0;
        }
        else{
            tmp++;
            
        }
    }
    if(tmp)
    {
        last_num = tmp;
    }
    return last_num;
}

int main(int arg, char *argv[])
{
    string s= "Hello World";
    int l = lengthOfLastWord(s);
    cout<<"l is "<<l;
}
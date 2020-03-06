#include<iostream>
#include<string>
using namespace std;

string init = "1";
string countAndSay(int n) {
    string result = init;
    
    for(int i = 0; i<n; i++)
    {
        string tmp="";
        char last = result[0];
        int repeat = 0;
        
        for(int j = 0;j < result.size();j++)
        {
            //cout<<repeat;
           if(result[j] == last)
            {
                repeat++;
            }
            else{
                tmp += to_string(repeat) +last;
                last = result[j];
                repeat = 1;
            }
            if(j==result.size()-1){
                tmp += to_string(repeat) +last;
                break;
            }
        }
        //cout<<tmp<<endl;

        result = tmp;
    }
    return result;
}

int main(int arg, char *argv[])
{
    int target = stoi(argv[1]);
string s = countAndSay(target);
cout<<s<<endl;
}
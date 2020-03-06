#include<iostream>
#include<vector>

using namespace std;
string longestCommonPrefix(vector<string>& strs) {
    int i = 0;
    
    string tmp =strs[0];
    for(i = 1; i< strs.size(); i++)
    {
        string same_str = "";
        int start_len = tmp.size();
        int  end_len = strs[i].size();
        int max_tmp = start_len<end_len?start_len:end_len;
         //cout<<max_tmp;
        for(int j =0; j<max_tmp;j++)
        {
            //cout<< "str"<<strs[i][j];
            //cout<< "tmp"<<tmp[j];
            if(strs[i][j] == tmp[j])
            {
                same_str += tmp[j];
            }
            else{
                break;
            }
        }
        tmp = same_str;
    }
    cout<<tmp;
}

int main()
{
    vector<string> strs = {"aca","cba"};
    longestCommonPrefix(strs);
    return 0;
}
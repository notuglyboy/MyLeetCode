#include<iostream>
#include<vector>

using namespace std;
int removeDuplicates(vector<int>& nums) {
        
        if(nums.size()<2)
            return nums.size();
        int last_num=888888;
        for(vector<int>::iterator iter = nums.begin();iter != nums.end();)
        {
            if(*iter == last_num)
            {
                last_num = *iter;
                iter = nums.erase(iter);
                
            }
            else
            {
                last_num = *iter;
                iter++;
            }

        }
}
int main()
{
    vector<int> nums = {0,0,1,1, 2};
    removeDuplicates(nums);
    for(auto i: nums)
        cout<<i<<' ';
    return 0;
}
#include<iostream>
#include<vector>

using namespace std;
int removeElement(vector<int>& nums, int val) {
        if (nums.size() == 0) return 0;
    int i = 0;
    for (int j = 0; j < nums.size(); j++) {
        if(nums[j]!=val)
        {
            nums[i] = nums[j];
            i++;
        }
    }

    return i;
    
    }
int main()
{

vector<int> nums = {3, 2,2,3};
int n = removeElement(nums, 3);
cout<<"return n "<<n<<endl;
for(int i =0;i<n;i++)
    cout<<nums[i]<<' ';
}
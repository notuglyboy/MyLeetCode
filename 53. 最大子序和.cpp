#include <iostream>
#include <vector>
using namespace std;

string init = "1";


#define INT_MAX 2147483647
#define INT_MIN -2147483648
int crosscalculate(vector<int>& nums, int start, int mid, int end)
{
        int left_max = INT_MIN;
        int right_max = INT_MIN;
        int tmp = 0;

        for(int i = mid; i>=start; i--)
        {
                tmp += nums[i];
                left_max = left_max > tmp?left_max:tmp;
        }
        tmp = 0;
        for(int i = mid + 1; i<=end; i++)
        {
                tmp += nums[i];
                right_max = right_max > tmp?right_max:tmp;
        }
        return right_max + left_max;
}

int mergeHelper(vector<int>& nums, int start, int end)
{
        int mid = (start + end) /2;
       if(start == end)
        return nums[start];
        int left_max = mergeHelper(nums, start, mid);
        int cross_num = crosscalculate(nums, start, mid, end);
        int right_max = mergeHelper(nums, mid+1, end);

        int tmp = left_max > right_max? left_max: right_max;
        int max = tmp > cross_num ? tmp: cross_num;
        return max;
}
int maxSubArray(vector<int>& nums) {
                int end = nums.size();
                int r =  mergeHelper(nums, 0 ,end-1);
                return r;
    }
int main()
{
    vector<int> nums = {-2,1,-3,4,-1,2,1,-5,4};
    int max = maxSubArray(nums);
    cout<<max;
}
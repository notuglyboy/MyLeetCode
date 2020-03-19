#include<iostream>
#include<vector>
using namespace std;

int searchInsert(vector<int>& nums, int target) {
    int mid_index;
    int start = 0;
    int end = nums.size() - 1;
    if(target > nums[end])
    {
        return end+1;
    }
    if(target < nums[start])
    {
        return start;
    }
    while(end > start)
    {
        mid_index = (end + start) / 2;
        //cout<<start<<' '<<end<<' '<<mid_index<<endl;

        if(nums[mid_index] < target)
        {
            start = mid_index + 1;
            
            
        }
        else{
            end = mid_index;

        }

    }
    return start;
}

int main(int arg, char *argv[])
{
    int target = stoi(argv[1]);
    vector<int> nums = {1, 3, 5, 6};
    int index = searchInsert(nums, target);
    cout<<index<<" target "<<target;
}


def find_distributor_level(level_range_list, target):
    list_len = len(level_range_list)
    i = 0
    start = 0
    end = len(level_range_list) - 1
    while start <= end:
        mid = int((start + end) / 2)
        if level_range_list[mid] < target:
            start = mid + 1
        elif level_range_list[mid] > target:
            end = mid - 1
        else:
            return mid
    return start
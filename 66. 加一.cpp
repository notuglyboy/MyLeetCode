#include <iostream>
#include <vector>
using namespace std;


vector<int> plusOne(vector<int>& digits) {
    int len = digits.size();
    
    if(digits[len-1] != 9)
    {
        digits[len-1] += 1;
        return digits;
    }
    int jin = 1;
    for(int i = len-1; i>= 0; i--)
    {
        digits[i] += jin;
        if(digits[i] == 10)
        {
            jin = 1;
            digits[i] = 0;
        }
        else{
            jin = 0;
        }
            
    }
    if(jin == 1)
    {
        digits.insert(digits.begin(), 1);
    }
    return digits;
}

int main(int arg, char *argv[])
{
    vector<int> nums = {2,4,9,3,9};
    plusOne(nums);
    for(auto i:nums)
        cout<<i<<',';
    cout<<endl;
    
}
#include<stdio.h>
#include <stdlib.h>
#include <string.h>
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    int max = 0;
    for(int i=0; i<numsSize; i++)
    {
        if(*(nums+i) > max)
        {
            max = *(nums+i);
        }
    }
    returnSize = (int *)malloc(sizeof(int) * 2);
    int *int_key = (int *)malloc(sizeof(int) * (max+1));
    int index = 0;
    memset(int_key, 0, sizeof(int) * (max+1));
    for(int i=0; i<numsSize; i++)
    {
        *(int_key + nums[i]) = i;
    }
    for(int i=0; i<numsSize; i++)
    {
        
        int distance = target - nums[i];

        if(distance < (max+1) && int_key[distance] != 0)
        {
            returnSize[0] = i;
            returnSize[1] = int_key[distance];
            return returnSize;
        }            
    }
    return returnSize;
}
int main(int arg, char *argv[])
{
    int target = atoi(argv[1]);
    int nums[4] = {-3,4,3,90};
    int *returnSize = NULL;
    int numsSize = sizeof(nums) / sizeof(int);
    int *re = twoSum(nums, numsSize, target, returnSize);
    printf("re1 %d, re2 %d", re[0], re[1]);
}
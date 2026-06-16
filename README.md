# Leetcode-solutions-DS
A continous journey to master the algrithms and to improve the logic building and problem-solving skills .solving daily challenges to build deep expertise in Data Structure.Arrays,and Logic using c 
/**
 * Problem: Two Sum (LeetCode #1)
 * Link: https://leetcode.com/problems/two-sum/
 * * Description: Find two numbers in an array that add up to a specific target.
 */
 static int result[2]; 

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    
    *returnSize = 2; 
    
    for (int i = 0; i < numsSize; i++) {
        for (int j = i + 1; j < numsSize; j++) {
            
            if (nums[i] + nums[j] == target) {
                result[0] = i; 
                result[1] = j; 
                return result; 
            }
        }
    }
    
    return 0;
}

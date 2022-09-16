/******************************************************
 *
 *  LeetCode Problem 1: Two Sum solution c++
 *
 *  Joel M. Gonzalez Rodriguez
 *
*/*****************************************************

vector<int> twoSum(vector<int>& nums, int target) 
{
    vector<int> arr;
        
    for(int i=0; i<nums.size(); i++)
        for(int j=i+1; j<nums.size(); j++)
        {
            if(nums[j]+nums[i] == target)
            {
                arr.push_back(i);
                arr.push_back(j);
                    
                return arr;
            }
        }
    return arr;
}

/*****************************************************
 *
 *  977. Squares of a Sorted Array solution c++
 *
 *  Joel M. Gonzalez Rodriguez
 *
*/****************************************************

vector<int> sortedSquares(vector<int>& nums) 
{            
    for(int i=0; i<nums.size(); i++)
        nums[i] = (nums[i] * nums[i]);            
            
    sort(nums.begin(), nums.end());;
        
    return nums;
}

/*****************************************************
 *
 *  704. Binary Search solution c++
 *
 *  Joel M. Gonzalez Rodriguez
 *
*/****************************************************

int search(vector<int>& nums, int target) 
{
    int l,r;
    l = 0; 
    r = nums.size()-1;
        
    while(l<=r)
    {
        int m = l+(r-l)/2;
            
        if(nums[m] == target)
            return m;
            
        else if(nums[m] < target)
            l = m+1;
            
        else
            r = m-1;
    }
        
    return -1;
}

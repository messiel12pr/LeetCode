/*****************************************************
 *
 *  35. Search Insert Position solution c++
 *
 *  Joel M. Gonzalez Rodriguez
 *
*/****************************************************

int searchInsert(vector<int>& nums, int target) 
{
    int l, r, m;
        
    l = 0;
    r = nums.size()-1;
        
    while(l<=r)
    {
        m = l+(r-l)/2;
            
        if(nums[m] == target)
            return m;   
                
        else if(nums[m] < target)
            l = m+1;
            
        else
            r = m-1;            
    }
        
    return l;
}

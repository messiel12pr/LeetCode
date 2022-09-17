/******************************************************
 *
 *  26. Remove Duplicates from Sorted Array solution c++
 *  
 *  Using set
 *
 *  Joel M. Gonzalez Rodriguez
 *
*/*****************************************************

int removeDuplicates(vector<int>& nums) 
{
    set<int> mySet;
    int size = nums.size();
        
    for(int i=0; i<size; i++)
        mySet.insert(nums[i]);
        
    std::copy(mySet.begin(), mySet.end(), nums.begin());
        
    return (size-(size-mySet.size()));
}

/*****************************************************
 *
 *  217. Contains Duplicate solution c++
 *
 *  Using Set
 *
 *  Joel M. Gonzalez Rodriguez
 *
*/****************************************************

bool containsDuplicate(vector<int>& nums) 
{
    set<int> mySet;
        
    for(int i=0; i<nums.size(); i++)
        mySet.insert(nums[i]);
        
    if(mySet.size()<nums.size())
        return true;
        
    else
        return false;
}

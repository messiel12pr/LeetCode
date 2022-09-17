/******************************************************
 *
 *  2395. Find Subarrays With Equal Sum solution c++
 *  
 *  Using hash map
 *
 *  Joel M. Gonzalez Rodriguez
 *
*/*****************************************************

bool findSubarrays(vector<int>& nums) 
{
    unordered_map<int, int> myMap;
        
    if(nums.size() >= 3)
    {
        if(nums.size()%2 == 0)
        {
            for(int i=0; i<nums.size()/2; i++)
               myMap.insert(make_pair(i,nums[i]+nums[i+1]));
        
            for(int i=0; i<nums.size()/2; i++)
                for(int j=i+1; j<nums.size()/2; j++)
                    if(myMap.at(i) == myMap.at(j))
                        return true;
            return false;
        }
            
        else
        {
            for(int i=0; i<(nums.size()/2)+1; i++)
                myMap.insert(make_pair(i,nums[i]+nums[i+1]));
        
            for(int i=0; i<(nums.size()/2)+1; i++)
                for(int j=i+1; j<(nums.size()/2)+1; j++)
                    if(myMap.at(i) == myMap.at(j))
                       return true;
            return false;
        }
                

    }
        
    else
        return false;
}

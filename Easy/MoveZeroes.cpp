/*****************************************************
 *
 *  283. Move Zeroes solution c++
 *
 *  Joel M. Gonzalez Rodriguez
 *
*/****************************************************

void moveZeroes(vector<int>& nums) 
{
    if(nums.size() > 1)
        for(int i=0; i<nums.size(); i++)
            if(nums[i] == 0)
                for(int j=i; j<nums.size(); j++)
                    if(nums[j] != 0)
                    {
                        nums[i] = nums[j];
                        nums[j] = 0;
                        break;
                    }  
}

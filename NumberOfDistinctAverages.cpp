/*****************************************************
 *
 *  2465. Number of Distinct Averages solution c++
 *
 *  Using Set 
 *
 *  Joel M. Gonzalez Rodriguez
 *
*/****************************************************

int distinctAverages(vector<int>& nums) 
{
    set<float> avr;
    sort(nums.begin(), nums.end());
  
    for(int i = 0; i<nums.size()/2; i++)
    {
        avr.insert((nums[i]+nums[(nums.size()-i)-1])/2.0);
    }
    return avr.size();
}

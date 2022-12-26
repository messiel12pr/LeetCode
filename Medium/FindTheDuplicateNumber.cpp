/*****************************************************
 *
 *  287. Find the Duplicate Number solution c++
 *
 *  Joel M. Gonzalez Rodriguez
 *
*/****************************************************

int findDuplicate(vector<int>& nums) 
{
    vector<int> temp(nums);

    sort(temp.begin(), temp.end());
        
    for(int i = 0; i<temp.size(); i++)
    {
        if(temp[i] == temp[i+1])
            return temp[i];
    }
    return 0;
}

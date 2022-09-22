/*****************************************************
 *
 *  136. Single Number solution c++
 *
 *  Using unordered_map
 *
 *  Joel M. Gonzalez Rodriguez
 *
*/****************************************************

int singleNumber(vector<int> &nums)
{
    unordered_map<int, int> myMap;
    int ans = 0;

    for (int i : nums)
        myMap[i]++;

    for (int i = 0; i < nums.size(); i++)
        if (myMap.at(nums[i]) == 1)
        {
            ans = nums[i];
            break;
        }

    return ans;
}

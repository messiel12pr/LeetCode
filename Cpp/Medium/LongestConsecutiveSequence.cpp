/*****************************************************
 *
 *  128. Longest Consecutive Sequence solution c++
 *
 *  Using set
 *
 *  Joel M. Gonzalez Rodriguez
 *
*/****************************************************

int longestConsecutive(vector<int> &nums)
{
    unordered_set<int> s;
    int max = 0;

    for (auto i : nums)
        s.insert(i);

    for (int i = 0; i < nums.size(); i++)
    {
        if (s.find(nums[i] - 1) == s.end())
        {
            int temp = 1;

            while (s.find(nums[i] + temp) != s.end())
                temp++;

            if (temp > max)
                max = temp;
        }
    }
    return max;
}

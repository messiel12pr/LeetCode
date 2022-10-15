/*****************************************************
 *
 *  1929. Concatenation of Array solution c++
 *
 *  Joel M. Gonzalez Rodriguez
 *
*/****************************************************

vector<int> getConcatenation(vector<int> &nums)
{
    vector<int> ans(nums.size() * 2);

    for (int i = 0; i < ans.size(); i++)
    {
        if (i == ans.size() / 2)
        {
            for (int j = 0; j < ans.size() / 2; j++)
            {
                ans[i] = nums[j];
                i++;
            }

            break;
        }

        ans[i] = nums[i];
    }

    return ans;
}

/*****************************************************
 *
 *  167. Two Sum II solution c++
 *
 *  Joel M. Gonzalez Rodriguez
 *
*/****************************************************

vector<int> twoSum(vector<int> &numbers, int target)
{
    vector<int> ans;
    int f, l;
    f = 0;
    l = numbers.size() - 1;

    while (f < l)
    {
        if (numbers[f] + numbers[l] == target)
        {
            ans.push_back(f + 1);
            ans.push_back(l + 1);

            return ans;
        }

        else if (numbers[f] + numbers[l] > target)
            l--;

        else
            f++;
    }

    return ans;
}

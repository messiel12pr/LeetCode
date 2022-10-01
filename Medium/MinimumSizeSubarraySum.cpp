/**********************************************************
 *
 *  209. Minimum Size Subarray Sum solution c++
 *
 *  Joel M. Gonzalez Rodriguez
 *
*/*********************************************************

int minSubArrayLen(int target, vector<int> &nums)
{
    int l, r, ans, sum;
    l = r = sum = 0;
    ans = INT_MAX;

    while (r < nums.size())
    {
        sum += nums[r];
        while (sum >= target)
        {
            ans = min(ans, (r - l) + 1);
            sum -= nums[l];
            l++;
        }
        r++;
    }

    if (ans == INT_MAX)
        return 0;

    else
        return ans;
}

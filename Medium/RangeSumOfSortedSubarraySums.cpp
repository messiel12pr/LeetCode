/**********************************************************
 *
 *  1508. Range Sum of Sorted Subarray Sums solution c++
 *
 *  Joel M. Gonzalez Rodriguez
 *
*/*********************************************************

int rangeSum(vector<int> &nums, int n, int left, int right)
{
    vector<int> arr;
    long int ans, 
    int l, r;
    ans = l = r = 0;

    while (l < nums.size())
    {

        if (r < nums.size())
        {
            ans += nums[r];
            arr.push_back(ans);
            r++;
        }

        else
        {
            ans = 0;
            l++;
            r = l;
        }
    }

    sort(arr.begin(), arr.end());

    for (int i = left - 1; i < right; i++)
    {
        ans += arr[i];
    }

    return ans % 1000000007;
}

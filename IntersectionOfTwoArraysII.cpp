/*****************************************************
 *
 *  350. Intersection of Two Arrays II solution c++
 *
 *  Joel M. Gonzalez Rodriguez
 *
*/****************************************************

vector<int> intersect(vector<int> &nums1, vector<int> &nums2)
{
    vector<int> ans;

    sort(nums1.begin(), nums1.end());
    sort(nums2.begin(), nums2.end());

    int l, r;
    l = r = 0;

    while (l < nums1.size() && r < nums2.size())
    {
        if (nums1[l] == nums2[r])
        {
            ans.push_back(nums1[l]);
            l++;
            r++;
        }

        else if (nums1[l] < nums2[r])
            l++;

        else
            r++;
    }
    return ans;
}

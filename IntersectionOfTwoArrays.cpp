/*****************************************************
 *
 *  349. Intersection of Two Arrays solution c++
 *
 *  Joel M. Gonzalez Rodriguez
 *
*/****************************************************

vector<int> intersection(vector<int> &nums1, vector<int> &nums2)
{
    vector<int> ans;
    int l, r;
    l = r = 0;

    sort(nums1.begin(), nums1.end());
    sort(nums2.begin(), nums2.end());

    while (l < nums1.size() && r < nums2.size())
    {
        if (nums1[l] == nums2[r])
        {

            if (ans.size() == 0)
                ans.push_back(nums1[l]);

            if (ans.size() != 0 && ans[ans.size() - 1] != nums1[l])
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

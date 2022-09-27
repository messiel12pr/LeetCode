/*****************************************************
 *
 *  392. Is Subsequence solution c++
 *
 *  Joel M. Gonzalez Rodriguez
 *
*/****************************************************

bool isSubsequence(string s, string t)
{
    int l, r, ans;
    l = 0;
    r = 0;
    ans = 0;

    while (l < s.length() && r < t.length())
    {
        if (t[r] == s[l])
        {
            r++;
            l++;
            ans++;
        }

        else
            r++;
    }

    return ans == s.length();
}

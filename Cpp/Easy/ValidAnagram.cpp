/****************************************
 *
 *  242. Valid Anagram solution c++
 *
 *  Joel M. Gonzalez Rodriguez
 *
*/***************************************

bool isAnagram(string s, string t)
{
    int l, r;
    l = r = 0;

    if (s.length() != t.length())
        return false;

    sort(s.begin(), s.end());
    sort(t.begin(), t.end());

    while (l < s.length() && r < t.length())
    {
        if (s[l] != t[r])
            return false;

        l++;
        r++;
    }

    return true;
}

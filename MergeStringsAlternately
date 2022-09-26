/*****************************************************
 *
 *  1768. Merge Strings Alternately solution c++
 *
 *  Joel M. Gonzalez Rodriguez
 *
*/****************************************************

string mergeAlternately(string word1, string word2)
{
    string ans;
    int l, r;
    l = 0;
    r = 0;

    if (word1.length() == word2.length())
    {
        while (l < word1.length() && r < word2.length())
        {
            ans += word1[l];
            ans += word2[r];
            l++;
            r++;
        }
    }

    else if (word1.length() > word2.length())
    {
        while (r < word2.length())
        {
            ans += word1[l];
            ans += word2[r];
            l++;
            r++;
        }

        while (l < word1.length())
        {
            ans += word1[l];
            l++;
        }
    }

    else
    {
        while (l < word1.length())
        {
            ans += word1[l];
            ans += word2[r];
            l++;
            r++;
        }

        while (r < word2.length())
        {
            ans += word2[r];
            r++;
        }
    }

    return ans;
}

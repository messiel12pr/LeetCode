/*****************************************************
 *
 *  917. Reverse Only Letters solution c++
 *
 *  Joel M. Gonzalez Rodriguez
 *
*/****************************************************

string reverseOnlyLetters(string s)
{
    int l, r;
    l = 0;
    r = s.length() - 1;

    while (l < r)
    {
        if (!(isalpha(s[l])))
            l++;

        if (!(isalpha(s[r])))
            r--;

        if (isalpha(s[l]) && isalpha(s[r]))
        {
            int temp = s[l];
            s[l] = s[r];
            s[r] = temp;
            l++;
            r--;
        }
    }

    return s;
}

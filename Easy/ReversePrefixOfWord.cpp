/*****************************************************
 *
 *  2000. Reverse Prefix of Word solution c++
 *
 *  Joel M. Gonzalez Rodriguez
 *
*/****************************************************

string reversePrefix(string word, char ch)
{
    int size, l, r;
    l = 0;
    r = 1;
    size = word.length();

    if (size == 1)
        return word;

    while (l < r && r < size)
    {
        if (word[r] == ch && word[l] != ch)
        {
            while (l < r)
            {
                int temp = word[l];
                word[l] = word[r];
                word[r] = temp;
                l++;
                r--;
            }
            return word;
        }

        else
            r++;
    }
    return word;
}

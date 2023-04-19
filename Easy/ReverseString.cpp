/*****************************************************
 *
 *  344. Reverse String solution c++
 *
 *  Joel M. Gonzalez Rodriguez
 *
*/****************************************************

void reverseString(vector<char>& s) 
{
    int l,r;
    l = 0;
    r = s.size()-1;
        
    while(l<r)
    {
        char temp = s[r];
        s[r] = s[l];
        s[l] = temp;
        l++;
        r--;
    }
}

/*****************************************************
 *
 *  125. Valid Palindrome solution c++
 *
 *  Joel M. Gonzalez Rodriguez
 *
*/****************************************************

bool isPalindrome(string s) 
{
    int l,r;
    l = 0;
    r = s.length();
        
    transform(s.begin(), s.end(), s.begin(), ::tolower);
        
    while(l<=r)
    {            
        if(!isalpha(s[l]) && !isdigit(s[l]))
        {
            l++; 
            continue;
        }
            
        if(!isalpha(s[r]) && !isdigit(s[r]))
        {
            r--;
            continue;
        }

            
        if(s[l] != s[r])
            return false;
            
         l++;
         r--;
    }
        
    return true;
}

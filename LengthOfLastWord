/******************************************************
 *
 *  LeetCode Problem 58: Length of last word solution c++
 *
 *  Joel M. Gonzalez Rodriguez
 *
*/*****************************************************

int lengthOfLastWord(string s) 
{
    int c = 0;
        
    for(int i=s.length()-1; i>=0; i--)
    {
        if(!iswalnum(s[i]) && c == 0)
            continue;
            
        else if(iswalnum(s[i]))
            c++;
            
        else
            return c;
    }      
    return c;
}

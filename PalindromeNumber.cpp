/******************************************************
 *
 *  LeetCode Problem 9: Palindrome Number solution c++
 *
 *  Joel M. Gonzalez Rodriguez
 *
*/*****************************************************

bool isPalindrome(int x) 
{
    bool found = false;

    std::string str = std::to_string(x);
        
    if(str.length() == 1)
        return true;
        
    for(int i=0; i<str.length()/2; i++)
    {
        if(str[i] == str[(str.length()-i)-1])
            found = true;
            
        else
            return false;
    }
        
    return found;
}

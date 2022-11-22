/*********************************************************
 *
 *  387. First Unique Character in a String solution c++
 *
 *  Using unordered map 
 *
 *  Joel M. Gonzalez Rodriguez
 *
*/********************************************************

int firstUniqChar(string s) 
{
    unordered_map<char, int> hm;

    for(int i = 0; i<s.length(); i++)
        hm[s[i]]++;

    for(int i = 0; i<s.length(); i++)
    {
        if(hm.find(s[i])->second == 1)
            return i;
    }
            
    return -1;
}

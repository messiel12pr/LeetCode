/*****************************************************
 *
 *  389. Find the Difference solution c++
 *
 *  Using unordered_map
 *
 *  Joel M. Gonzalez Rodriguez
 *
*/****************************************************

char findTheDifference(string s, string t) 
{
    unordered_map<char, int> myMap;
        
    for(int i=0; i<s.length(); i++)
        myMap[s[i]]++;
        
    for(int i=0; i<t.length(); i++)
        myMap[t[i]]++;
        
    for(int i=0; i<t.length(); i++)
        if(myMap.at(t[i])%2 == 1)
            return t[i];
    return -1;
}

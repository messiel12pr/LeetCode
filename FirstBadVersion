/*****************************************************
 *
 *  278. First Bad Version solution c++
 *
 *  Joel M. Gonzalez Rodriguez
 *
*/****************************************************

int firstBadVersion(int n) 
{
    int l, r, m;
        
    l = 1;
    r = n;
        
    while(l<=r)
    {
        int m = l+(r-l)/2;
            
        if(isBadVersion(m))
            r = m-1;
            
        else
            l = m+1;
            
    }
        
    return l;
}

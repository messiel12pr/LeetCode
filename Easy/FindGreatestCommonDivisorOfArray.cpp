/************************************************************
 *
 *  1979. Find Greatest Common Divisor of Array solution c++
 *
 *  Joel M. Gonzalez Rodriguez
 *
*/***********************************************************

int findGCD(vector<int>& nums) 
{
    int min = *min_element (nums.begin(), nums.end());
    int max = *max_element (nums.begin(), nums.end());
        
    return __gcd(min, max);
}

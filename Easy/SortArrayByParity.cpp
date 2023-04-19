/*****************************************************
 *
 *  905. Sort Array By Parity solution c++
 *
 *  Joel M. Gonzalez Rodriguez
 *
*/****************************************************

vector<int> sortArrayByParity(vector<int> &nums)
{
    int l, r, temp;
    l = 0;
    r = nums.size() - 1;

    while (l < r)
    {
        if (nums[r] % 2 == 0 && nums[l] % 2 == 1)
        {
            int temp = nums[l];
            nums[l] = nums[r];
            nums[r] = temp;
            l++;
            r--;
        }
        
        if (nums[r] % 2 == 1)
            r--;
            
        if (nums[l] % 2 == 0)
            l++;
    }
    
    return nums;
}

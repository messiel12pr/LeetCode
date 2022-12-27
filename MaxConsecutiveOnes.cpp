/*****************************************************
 *
 *  485. Max Consecutive Ones solution c++
 *
 *  Joel M. Gonzalez Rodriguez
 *
*/****************************************************

int findMaxConsecutiveOnes(vector<int> &nums)
{
    int temp = 0;
    int m = 0;

    for (auto i : nums)
    {
        if (i == 0)
        {
            if (temp > m)
                m = temp;
            temp = 0;
        }

        if (i == 1)
            temp++;
    }

    return max(temp, m);
}

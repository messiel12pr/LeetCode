/*****************************************************
 *
 *  121. Best Time to Buy and Sell Stock solution c++
 *
 *  Joel M. Gonzalez Rodriguez
 *
*/****************************************************

int maxProfit(vector<int> &prices)
{
    int l, r, profit, high;
    l = profit = high = 0;
    r = 1;

    while (r < prices.size())
    {
        if (prices[l] < prices[r])
        {
            profit = prices[r] - prices[l];
            high = max(high, profit);
        }

        else
            l = r;
        r++;
    }

    return high;
}

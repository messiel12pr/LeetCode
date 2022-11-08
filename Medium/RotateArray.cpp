/*******************************
 *
 *  189. Rotate Array
 *
 *  Using dq
 *
 *  Joel M. Gonzalez Rodriguez
 *
*/******************************

void rotate(vector<int> &nums, int k)
{
    deque<int> dq;
    int size = nums.size();

    for (int i = 0; i < size; i++)
    {
        dq.push_back(nums[i]);
    }

    for (int i = 0; i < k; i++)
    {
        int temp = dq.back();
        dq.pop_back();
        dq.push_front(temp);
    }

    for (int i = 0; i < size; i++)
    {
        int temp = dq.front();
        dq.pop_front();
        nums[i] = temp;
    }
}

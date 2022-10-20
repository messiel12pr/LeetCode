/*****************************************************
 *
 *  496. Next Greater Element I solution c++
 *
 *  Using Stack
 *
 *  Joel M. Gonzalez Rodriguez
 *
*/****************************************************

vector<int> nextGreaterElement(vector<int> &nums1, vector<int> &nums2)
{
    bool found;
    int element;

    for (int i = 0; i < nums1.size(); i++)
    {
        stack<int> myStack;
        element = nums1[i];
        found = false;
        for (int j = 0; j < nums2.size(); j++)
        {
            myStack.push(nums2[j]);

            if (myStack.top() == nums1[i])
                found = true;

            if (found && myStack.top() > nums1[i])
            {
                nums1[i] = myStack.top();
                break;
            }
        }

        if (element == nums1[i])
            nums1[i] = -1;
    }

    return nums1;
}

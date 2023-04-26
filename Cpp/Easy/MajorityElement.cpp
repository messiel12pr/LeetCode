/*****************************************************
 *
 *  169. Majority Element solution c++
 *
 *  Using unordered_map
 *
 *  Joel M. Gonzalez Rodriguez
 *
*/****************************************************

int majorityElement(vector<int> &nums)
{
    unordered_map<int, int> myMap;

    for (int i : nums)
        myMap[i]++;

    pair<int, int> maxValuePair;
    int maxValue = INT_MIN;

    for (const auto &entry : myMap)
    {
        if (maxValue < entry.second)
        {
            maxValue = entry.second;
            maxValuePair = entry;
        }
    }

    return maxValuePair.first;
}

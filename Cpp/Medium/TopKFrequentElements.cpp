/*****************************************************
 *
 *  347. Top K Frequent Elements solution c++
 *
 *  Using hash map and priority queue 
 *  
 *  Joel M. Gonzalez Rodriguez
 *
*/****************************************************

vector<int> topKFrequent(vector<int> &nums, int k)
{
    unordered_map<int, int> hm;
    priority_queue<pair<int, int>> pq;
    vector<int> ans;

    for (auto i : nums)
        hm[i]++;

    for (auto i : hm)
    {
        pq.push(make_pair(i.second, i.first));
    }

    for (int i = 0; i < k; i++)
    {
        ans.push_back(pq.top().second);
        pq.pop();
    }
    return ans;
}

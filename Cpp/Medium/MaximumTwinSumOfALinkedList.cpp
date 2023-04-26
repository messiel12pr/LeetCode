/*****************************************************
 *
 *  2130. Maximum Twin Sum of a Linked List solution c++
 *
 *  Using deque
 *
 *  Joel M. Gonzalez Rodriguez
 *
*/****************************************************

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

int pairSum(ListNode *head)
{
    int max = INT_MIN, temp = 0;
    ListNode *current = head;
    deque<int> dq;

    while (current != nullptr)
    {
        dq.push_back(current->val);
        current = current->next;
    }

    while (dq.size() != 0)
    {
        temp = dq.front() + dq.back();
        if (temp > max)
            max = temp;

        dq.pop_front();
        dq.pop_back();
    }

    return max;
}

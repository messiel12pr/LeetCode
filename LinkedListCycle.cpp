/*****************************************************
 *
 *  141. Linked List Cycle solution c++
 *
 *  Using hash map
 *
 *  Joel M. Gonzalez Rodriguez
 *
*/****************************************************

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

bool hasCycle(ListNode *head) 
{
    ListNode *current = head;
    unordered_map<ListNode*, int> hm;

    while(current != nullptr)
    {
        if(!hm.count(current))
            hm[current]++;

        else 
            return true;

        current = current->next;
    }

    return false;
}

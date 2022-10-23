/*****************************************************
 *
 *  203. Remove Linked List Elements solution c++
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

ListNode *removeElements(ListNode *head, int val)
{
    ListNode *prev, *current;
    current = head;

    if (head == nullptr)
        return head;

    while (current != nullptr)
    {
        if (current->val == val && head == current)
        {
            current = current->next;
            head = current;
        }

        else if (current->val == val && head != current)
        {
            prev->next = current->next;
            current = current->next;
        }

        else
        {
            prev = current;
            current = current->next;
        }
    }

    return head;
}

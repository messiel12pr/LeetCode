/*****************************************************
 *
 *  876. Middle of the Linked List solution c++
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

ListNode *middleNode(ListNode *head)
{
    ListNode *l;
    int c = 0;
    ;
    l = head;

    while (l != nullptr)
    {
        l = l->next;
        c++;
    }

    l = head;

    for (int i = 0; i < c / 2; i++)
    {
        l = l->next;
    }

    return l;
}

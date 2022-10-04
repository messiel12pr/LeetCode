/*****************************************************
 *
 *  1290. Convert Binary Number in a Linked List to Integer solution c++
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

int getDecimalValue(ListNode *head)
{
    ListNode *current;
    int c, ans;
    c = ans = 0;
    current = head;

    while (current != nullptr)
    {
        current = current->next;
        c++;
    }

    current = head;

    for (int i = c - 1; c > 0; c--)
    {
        if (current->val == 1)
            ans += pow(2, c);

        current = current->next;
    }

    return ans / 2;
}

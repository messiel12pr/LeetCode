/*****************************************************
 *
 *  206. Reverse Linked List solution c++
 *
 *  Using Stack 
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

ListNode *reverseList(ListNode *head)
{
    ListNode *current = head;
    stack<int> myStack;

    while (current != nullptr)
    {
        myStack.push(current->val);
        current = current->next;
    }

    int size = myStack.size();
    current = head;

    for (int i = 0; i < size; i++)
    {
        current->val = myStack.top();
        myStack.pop();
        current = current->next;
    }

    return head;
}

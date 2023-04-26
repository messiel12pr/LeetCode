/*****************************************************
 *
 *  143. Reorder List solution c++
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
 
void reorderList(ListNode *head)
{
    stack<ListNode *> myStack;
    ListNode *current = head;

    while (current != nullptr)
    {
        myStack.push(current);
        current = current->next;
    }

    current = head;
    int size = myStack.size();

    for (int i = 0; i < size; i++)
    {
        if (i % 2 == 0)
        {
            ListNode *temp = myStack.top();
            temp->next = current->next;
            current->next = temp;
            myStack.pop();
        }

        current = current->next;

        if (i == size - 1)
            current->next = nullptr;
    }
}

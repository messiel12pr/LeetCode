/*****************************************************
 *
 *  237. Delete Node in a Linked List solution c++
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
 
void deleteNode(ListNode* node) 
{
    node->val = node->next->val;
    node->next = node->next->next;
}

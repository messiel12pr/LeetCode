/*********************************************************
 *
 *  83. Remove Duplicates from Sorted List solution c++
 *
 *  Joel M. Gonzalez Rodriguez
 *
*/********************************************************

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

bool deleteNode(ListNode *head)
{
    ListNode *current, *prev;
    current=prev=head;
        
    while(current->next != nullptr)
    {
        prev = current;
        current = current->next; 
            
        if(prev->val == current->val)
        {
            prev->next = current->next;
            delete current;
                
            return true;
        }      
    }
    
    return false;
}
    
ListNode* deleteDuplicates(ListNode* head) 
{   
    if(head == nullptr)
        return head;
        
    while(deleteNode(head))
        deleteNode(head);
        
    return head;
}

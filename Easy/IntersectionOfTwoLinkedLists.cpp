/**
 * 
 *  160. Intersection of Two Linked Lists
 *
 *  Joel M. Gonzalez Rodriguez
 * 
 *  Definition for singly-linked list.
 *  struct ListNode {
 *      int val;
 *      ListNode *next;
 *      ListNode(int x) : val(x), next(NULL) {}
 *  };
 * 
 */

class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) 
    {
        int size = 0;
        set<ListNode*> s;

        while(headA != nullptr || headB != nullptr)
        {   
            if(headA != nullptr) 
            {
                s.insert(headA);
                size++;
                if(s.size() != size)
                    return headA;
                headA = headA->next;
            }

            if(headB != nullptr)
            {
                s.insert(headB);
                size++;
                if(s.size() != size)
                    return headB;   
                headB = headB->next;             
            }
        }
        return nullptr;
    }
};
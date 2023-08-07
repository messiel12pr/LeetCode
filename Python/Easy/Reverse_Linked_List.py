'''
    
    206. Reverse Linked List

    Solution:

'''

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head

        prev_node = head
        head = head.next
        prev_node.next = None
        
        while head != None:
            new_node = ListNode()
            new_node.val = head.val
            new_node.next = prev_node
            prev_node = new_node

            head = head.next
            
        return prev_node
'''

    19. Remove Nth Node From End of List

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        i = 0

        while temp:
            temp = temp.next
            i += 1



        temp = head
        for _ in range(i - n - 1):
            temp = temp.next
            
        if i - n == 0:
            head = head.next
            return head

        temp.next = temp.next.next
        return head
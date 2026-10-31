'''

    21. Merge Two Sorted Lists

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return list1

        elif not list1:
            return list2

        elif not list2:
            return list1

        slow_ptr_1, ptr_1, ptr_2 = list1, list1, list2
        head = list1
        while ptr_1 and ptr_2:
            if ptr_1.val > ptr_2.val:
                new_node = ListNode(ptr_2.val)
                new_node.next = ptr_1
                
                if ptr_1 == head:
                    head = new_node
                    slow_ptr_1 = new_node

                else:
                    slow_ptr_1.next = new_node
                    slow_ptr_1 = slow_ptr_1.next

                ptr_2 = ptr_2.next

            elif ptr_1.val < ptr_2.val:
                while ptr_1 and ptr_1.val < ptr_2.val:
                    slow_ptr_1 = ptr_1
                    ptr_1 = ptr_1.next

                if not ptr_1:
                    slow_ptr_1.next = ptr_2
                    return head

            else:
                new_node = ListNode(ptr_2.val)
                new_node.next = ptr_1.next
                ptr_1.next = new_node
                slow_ptr_1 = ptr_1
                ptr_1 = ptr_1.next 
                ptr_2 = ptr_2.next

        return head

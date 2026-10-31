'''

    2. Add Two Numbers

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry_on = 0
        head = None
        tail = head

        while l1 or l2:
            current_sum = 0
            
            if l1 and l2:
                new_node = ListNode()
                current_sum = l1.val + l2.val + carry_on

                if current_sum > 9:
                    carry_on = current_sum // 10
                    new_node.val = current_sum % 10

                else:
                    carry_on = 0
                    new_node.val = current_sum
                
                if not head:
                    new_node.next = None
                    head = new_node
                    tail = new_node

                else:
                    new_node.next = None
                    tail.next = new_node
                    tail = new_node

            elif l1 and not l2:
                while l1:
                    new_node = ListNode()
                    current_sum = l1.val + carry_on

                    if current_sum > 9:
                        carry_on = current_sum // 10
                        new_node.val = current_sum % 10

                    else:
                        carry_on = 0
                        new_node.val = current_sum

                    new_node.next = None
                    tail.next = new_node
                    tail = new_node

                    l1 = l1.next
            
                if carry_on > 0:
                    new_node = ListNode(carry_on)
                    new_node.next = None
                    tail.next = new_node
                    tail = new_node
                return head

            elif l2 and not l1:
                while l2:
                    new_node = ListNode()
                    current_sum = l2.val + carry_on

                    if current_sum > 9:
                        carry_on = current_sum // 10
                        new_node.val = current_sum % 10

                    else:
                        carry_on = 0
                        new_node.val = current_sum

                    new_node.next = None
                    tail.next = new_node
                    tail = new_node

                    l2 = l2.next

                if carry_on > 0:
                    new_node = ListNode(carry_on)
                    new_node.next = None
                    tail.next = new_node
                    tail = new_node
                return head

            l1 = l1.next
            l2 = l2.next

        if carry_on > 0:
            new_node = ListNode(carry_on)
            new_node.next = None
            tail.next = new_node
            tail = new_node

        return head
        

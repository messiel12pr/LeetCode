'''

    328. Odd Even Linked List

    Solution:

'''

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = None
        even = None
        even_head = None
        itr = None

        if head and head.next and head.next.next:
            odd = head
            even = head.next
            even_head = even
            itr = head.next.next

        else: return head

        flag = 0

        while itr:
            if flag == 0:
                odd.next = itr
                odd = odd.next
                flag = 1

            elif flag == 1:
                even.next = itr
                even = even.next
                flag = 0

            itr = itr.next

        even.next = None
        odd.next = even_head

        return head
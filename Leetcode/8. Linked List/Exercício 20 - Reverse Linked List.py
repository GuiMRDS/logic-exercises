class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_list = None

        while head:
            new_node = head.next
            head.next = new_list
            new_list = head
            head = new_node


        return new_list
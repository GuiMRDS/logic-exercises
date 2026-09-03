from Python.DSA.Outros.MergeSoft import ListNode


class Solution:
    def LinkedCycle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
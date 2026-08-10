---------------------CORE IDEA------------------

Save the next, flip the arrow, move both pointers forward.

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None          # Previous node (starts as None)
        curr = head          # Current node (starts at head)

        while curr:          # While there are still nodes to process
            temp = curr.next  # Save the next node (so we don't lose it)
            curr.next = prev  # Reverse the arrow: point curr to prev
            prev = curr       # Move prev forward
            curr = temp       # Move curr forward

        return prev          # prev is the new head

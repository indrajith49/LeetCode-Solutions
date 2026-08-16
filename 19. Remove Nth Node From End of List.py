-----------------------------CORE IDEA-------------------------

1. Create a dummy node before the original head. This eliminates the special edge case when we need to delete the head node.
2. Initialise slow and fast pointers — both start at the dummy node.
3. Move the fast pointer forward n steps alone. This creates a fixed gap of n nodes between slow and fast.
4. Now move both pointers one step at a time simultaneously, stop when fast.next == None.
~~~~~~At this moment, slow lands on the node immediately before the target node to delete.
5. Delete the target node: slow.next = slow.next.next
6. Return dummy.next (the real starting node of the modified linked list).
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy= ListNode(0)
        dummy.next=head

        slow = dummy
        fast = dummy

        for i in range(n):
            fast = fast.next


        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next

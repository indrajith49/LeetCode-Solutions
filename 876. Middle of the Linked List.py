----------------------CORE IDEA---------------------
1. We use two pointers starting at head;slow advances one step, fast advances two steps. 
2. The loop runs while fast and fast.next exist.
3. When the loop exits, slow points to the middle node.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow

  

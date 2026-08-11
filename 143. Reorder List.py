------------------------------------CORE IDEA--------------------------------

We cut the list into two halves, 
reverse the second half,
then merge them alternately 
— one node from the first half, one from the second half.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #first part is cut the list into half

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        prev = None
        curr = slow

        #then reverse second half
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        #merge one by one
        first = head
        second = prev

        while second.next:
            temp1 = first.next
            temp2 = second.next


            first.next = second
            second.next = temp1

            first = temp1
            second = temp2


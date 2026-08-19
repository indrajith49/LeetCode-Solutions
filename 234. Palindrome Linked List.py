-----------------CORE IDEA----------------
We are basically converting linked list to an array and then comparing. 



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        values = []

        while curr:
            values.append(curr.val)
            curr = curr.next


        left, right = 0, len(values) - 1

        while left < right:
            if values[left] != values[right]:
                return False
            left += 1
            right -= 1
        return True


------------------------USING LINKED LIST------------------

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        def reverse(head):

            prev = None
            curr = head
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next

            return prev
    #find the middle point
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half =  reverse(slow)


        p1 = head
        p2 = second_half
        
        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next    
            p2 = p2.next
        return True

























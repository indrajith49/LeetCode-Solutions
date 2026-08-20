-----------------------------------CORE IDEA---------------------------



#THERE IS ANOTHER BRUTE FORCE VERSION OF THIS WORKS KINDA SAME LIKE THISWS...
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        stackA = []
        stackB = []


        current = headA
        while current:
            stackA.append(current)
            current = current.next

        current = headB
        while current:
            stackB.append(current)
            current = current.next


        prev = None
        while stackA and stackB:
            nodeA = stackA.pop()
            nodeB = stackB.pop()
            if nodeA == nodeB:
                prev = nodeB
            else:
                break
        return prev

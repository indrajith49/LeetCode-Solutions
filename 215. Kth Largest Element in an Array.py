from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        result = []
        for i in range(n-1, 0,-1):
            result.append(nums[i])

        return result[k-1]

sol =Solution()
print(sol.findKthLargest([3,2,1,5,6,4], k = 2))

#ALTERNATIVE SOLUTION
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]

#HEAP's PERSPECTIVE -> FIRST PROBLEM I SOLVED MYSELF LMFAO AFTER SOLVING 46 LEETCODE PROBLEMS LMFAO

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        heap = []

        for num in nums:
            heapq.heappush(heap, num)

            while len(heap)>k:
                heapq.heappop(heap)

        return heap[0]
--------------------------------------------CORE IDEA------------------------------------------------------------------------
1. 1. we will return the heap[0] and before that we will make the list heaped and then keep only till the size of the heap is upto k. 
2. For that at the very beginning, we will make the heap heaped so that the smallest element always stays at the very beginning. 
3. If the size of the heap is greater than k we will pop from the left (the smallest element) and keep doing it till the size of the list is equal to k. 
4. And return the heap[0] which will be the smallest element of that k-sized list. 


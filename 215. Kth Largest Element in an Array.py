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

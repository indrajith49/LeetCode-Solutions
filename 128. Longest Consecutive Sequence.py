-------------------------------Brute Force-------------------------------
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        store = set(nums)

        for num in nums:
            streak, curr = 0, num
            while curr in store:
                streak += 1
                curr += 1
            res = max(res, streak)
        return res

------------------------------Brute Force-------------------------------
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||


------------------------------Sorting-------------------------------
from typing import List
class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        res = 0
        nums.sort()

        curr, streak = nums[0], 0
        i = 0
        while i<len(nums):
            if curr!=nums[i]:
                curr = nums[i]
                streak = 0

            while i < len(nums) and nums[i] == curr:
                i+=1
            streak+=1
            curr+=1

            res = max(res, streak)

        return res
sol = Solution()
print(sol.longestConsecutive([1, 2, 3, 4, 100, 200]))


------------------------------Sorting-------------------------------
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

------------------------------Hash Set-------------------------------
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        length = 0
        for num in numSet:
            if num-1 not in numSet:
                longest = 1
                while num+longest in numSet:
                    longest+=1
                length = max(longest , length)
        return length

------------------------------Hash Set-------------------------------
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||







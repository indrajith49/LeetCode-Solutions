from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        # i = position where we place the next valid element
        i = 2
        
        for j in range(2, len(nums)):
            # If current element is different from the element TWO positions behind
            if nums[j] != nums[i - 2]:
                nums[i] = nums[j]
                i += 1
        
        return i

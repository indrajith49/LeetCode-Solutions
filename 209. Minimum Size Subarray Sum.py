class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:  # target first, nums second        
        if not nums:
            return 0

        current_sum = 0
        min_value = float('inf')
        left = 0

        for right in range(len(nums)):
            current_sum+=nums[right]

            while current_sum>=target:
                min_value = min(min_value, right-left+1)

                current_sum-=nums[left]
                left+=1

        return 0 if min_value == float('inf') else min_value


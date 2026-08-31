-----------------------------CORE IDEA------------------------------
We use two pointers (left and right), both starting at 0. right expands the window by adding elements.
While the sum of the window is >= target, we update the minimum length, 
then shrink the window from the left by subtracting nums[left] and moving left forward.


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

                current_sum-=nums[left]
                min_value = min(min_value, right-left+1)

                left+=1

        return 0 if min_value == float('inf') else min_value
        #we can also write return like  this -> return min_value if min_val!=float('inf') else 0



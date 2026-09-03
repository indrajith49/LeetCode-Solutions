class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0
        curr_prod = 1
        left = 0
        for right in range(len(nums)):
            curr_prod *= nums[right]
            while curr_prod >= k:
                curr_prod //= nums[left]
                left += 1

            res += right - left + 1
        return res
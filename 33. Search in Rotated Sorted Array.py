-----------------------CORE IDEA--------------------
1. Compute `mid`. If `nums[mid]==target` return `mid`.
2. Check **which half is sorted**:
   - `if nums[l] <= nums[mid]`: Left half `[l ... mid]` is sorted
     - If target lies between `nums[l]` and `nums[mid]` → search left: `r = mid‑1`
     - Else → search right: `l = mid+1`
   - `else`: Right half `[mid ... r]` is sorted
     - If target lies between `nums[mid]` and `nums[r]` → search right: `l = mid+1`
     - Else → search left: `r = mid‑1`
3. Loop condition: `while l <= r`
4. If loop ends, target not found → return `-1`

> 
> Reference point: use `nums[l]` and `nums[r]` to check sorted segment bounds.



    
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r  = 0, n-1


        while l<=r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:  # Left half is sorted
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:  # Right half is sorted
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

sol = Solution()
print(sol.search([4,5,6,7,0,1,2], 1))

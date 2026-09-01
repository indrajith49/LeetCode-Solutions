-----------------------------------CORE IDEA--------------------------------

1. Loop condition: `while l < r` (stop when `l == r`)
2. Compute `mid`. Compare **`nums[mid] vs nums[r]`** (`nums[r]` is reliable reference, always in lower chunk)
   - `if nums[mid] > nums[r]`: mid is inside big upper chunk. Minimum is to the right of mid → `l = mid + 1`
   - `else`: subarray `[mid ... r]` is sorted. Minimum can be mid or left of mid → keep mid, set `r = mid`
3. When `l == r`, this index holds minimum value → return `nums[l]`

> 
> Reference point: only use `nums[r]`.
> Goal: **find pivot / smallest element**, no target.


with edge case
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        # Edge case: already sorted
        if nums[l] < nums[r]:
            return nums[l]
        
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[l]:
                r = mid
            else:
                l = mid + 1
        
        return nums[l]


Comparing with right
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        return nums[l]

  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
The Real Rule (For Finding Minimum):
In a rotated sorted array, the minimum is ALWAYS located in the UNSORTED half.

Think about it:

If you have a sorted array [1, 2, 3, 4, 5], the minimum 1 is at the start of the sorted array (no rotation).

If you have a rotated array [4, 5, 6, 7, 0, 1, 2], the minimum 0 is at the break point where the sorting stops.

The minimum sits at the boundary between the two sorted halves.

  ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
  Why Comparing with RIGHT Works So Well
The rightmost element (nums[r]) is the last element of the array. Because of the rotation, there are only two possibilities:

The array is perfectly sorted (no rotation): nums[mid] will NEVER be greater than nums[r]. So we keep moving left (r = mid) until we find the start.

The array is rotated: The rightmost element is part of the smaller, rotated half.

Here is the logic:
If nums[mid] > nums[r], it means the left half is sorted and the right half is unsorted. Since the minimum is in the unsorted half, we go RIGHT (l = mid + 1).
If nums[mid] <= nums[r], it means the right half is sorted. Since the minimum can't be in a sorted half (unless it's the very start), the minimum must be in the left half. We go LEFT (r = mid).

It works because nums[r] is part of the right half. By comparing mid to r, we can tell if the right half is sorted or not.







The "Fixed Rule" You Are Looking For
There is one fixed rule for this problem:

"Identify which half is unsorted, and search there for the minimum."

If the right half is unsorted (nums[mid] > nums[r]), the minimum is on the right (l = mid + 1).

If the left half is unsorted (nums[mid] < nums[l]), the minimum is on the left (r = mid).

---------------------------------------------CORE IDEA-----------------------------------------------
We move unique numbers forward by overwriting duplicates, and i + 1 gives us the count of unique numbers.
#NEED MORE DETAILED BREAKDOWN PLEASE


-------------------------------------------USING TWO POINTER---------------------------------------------
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Slow finger: where the next unique person should stand
        i = 0
        
        # Fast finger: walks through the line
        for j in range(1, len(nums)):
            # If we found a new person (not the same as the last unique)
            if nums[j] != nums[i]:
                # Move the slow finger forward
                i += 1
                # Place the new person here
                nums[i] = nums[j]
        
        # Number of unique people = slow finger + 1
        return i + 1

-------------------------------------------ALTERNATIVE WHICH I DONT KNOW YET-----------------------------------
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = sorted(set(nums))

        for i in range(len(unique)):
            nums[i] = unique[i]

        return len(unique)

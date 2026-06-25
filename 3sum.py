class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res


"""
LINE 1: res = []
Part	Explanation
What it does	Creates an empty list to store results
Why it's needed	We'll add all valid triplets here
Example	res = []
LINE 2: nums.sort()
Part	Explanation
What it does	Sorts the array in ascending order
Why it's needed	Two-pointer technique requires sorted array
Example	[-4, -1, -1, 0, 1, 2] → [-4, -1, -1, 0, 1, 2] (already sorted)
LINE 4: for i, a in enumerate(nums):
Part	Explanation
What it does	Loops through each element with its index
Why it's needed	i = index, a = value at that index (the first number of triplet)
Example	i=0, a=-4 → i=1, a=-1 → etc.
LINE 5: if a > 0:
Part	Explanation
What it does	If current number is positive, break
Why it's needed	Since array is sorted, all remaining numbers are positive. Three positive numbers can't sum to 0.
Example	nums = [-4, -1, -1, 0, 1, 2] → When a=1 (positive), break
LINE 6: break
Part	Explanation
What it does	Exits the loop
Why it's needed	No more valid triplets possible
LINE 8: if i > 0 and a == nums[i - 1]:
Part	Explanation
What it does	Checks if current number is same as previous
Why it's needed	To skip duplicate triplets
Example	nums = [-4, -1, -1, 0, 1, 2] → When i=2, a=-1, previous is also -1 → skip
LINE 9: continue
Part	Explanation
What it does	Skips current iteration and moves to next i
Why it's needed	Prevents duplicate triplets
LINE 11: l, r = i + 1, len(nums) - 1
Part	Explanation
What it does	Sets left pointer to next element, right pointer to last element
Why it's needed	Two-pointer technique to find pairs that sum to -a
Example	i=0, a=-4 → l=1, r=5
LINE 12: while l < r:
Part	Explanation
What it does	Loop until pointers cross
Why it's needed	Need to check all possible pairs
LINE 13: threeSum = a + nums[l] + nums[r]
Part	Explanation
What it does	Calculates sum of current triplet
Why it's needed	To check if it equals 0
Example	a=-4, nums[1]=-1, nums[5]=2 → -4 + -1 + 2 = -3
LINE 14: if threeSum > 0:
Part	Explanation
What it does	If sum is too big (positive)
Why it's needed	Need to reduce sum → move right pointer left (smaller numbers)
LINE 15: r -= 1
Part	Explanation
What it does	Moves right pointer left by one
Why it's needed	To decrease the sum
LINE 16-17: elif threeSum < 0:
Part	Explanation
What it does	If sum is too small (negative)
Why it's needed	Need to increase sum → move left pointer right (larger numbers)
LINE 18: l += 1
Part	Explanation
What it does	Moves left pointer right by one
Why it's needed	To increase the sum
LINE 19: else:
Part	Explanation
What it does	threeSum == 0 → Found a valid triplet!
LINE 20: res.append([a, nums[l], nums[r]])
Part	Explanation
What it does	Adds the triplet to results
Example	[-1, -1, 2] → res = [[-1, -1, 2]]
LINE 21: l += 1
Part	Explanation
What it does	Move left pointer right (to continue searching)
LINE 22: r -= 1
Part	Explanation
What it does	Move right pointer left (to continue searching)
LINE 23: while nums[l] == nums[l - 1] and l < r:
Part	Explanation
What it does	Skip duplicate values on the left
Why it's needed	To avoid duplicate triplets
Example	nums = [-4, -1, -1, 0, 1, 2] → Skip second -1
LINE 24: l += 1
Part	Explanation
What it does	Move left pointer past duplicates
LINE 26: return res
Part	Explanation
What it does	Returns all found triplets
Example	[[-1, -1, 2], [-1, 0, 1]]
Complete Trace: nums = [-4, -1, -1, 0, 1, 2]
text
Sorted: [-4, -1, -1, 0, 1, 2]
Index:    0   1   2  3  4  5

i=0, a=-4:
  l=1, r=5
  threeSum = -4 + (-1) + 2 = -3 → <0 → l=2
  threeSum = -4 + (-1) + 2 = -3 → <0 → l=3
  threeSum = -4 + 0 + 2 = -2 → <0 → l=4
  threeSum = -4 + 1 + 2 = -1 → <0 → l=5
  l=5, r=5 → loop ends
  No triplet found

i=1, a=-1:
  l=2, r=5
  threeSum = -1 + (-1) + 2 = 0 → FOUND!
    res.append([-1, -1, 2])
    l=3, r=4
    Skip duplicates: nums[3]=0, nums[2]=-1 → no skip
  threeSum = -1 + 0 + 1 = 0 → FOUND!
    res.append([-1, 0, 1])
    l=4, r=3 → loop ends

i=2, a=-1:
  i>0 and a == nums[1] (-1 == -1) → continue (skip duplicate)

i=3, a=0:
  l=4, r=5
  threeSum = 0 + 1 + 2 = 3 → >0 → r=4
  l=4, r=4 → loop ends

i=4, a=1:
  a>0 → break

Return: [[-1, -1, 2], [-1, 0, 1]] ✅
Summary Table:
Line	What it does	Why
res = []	Initialize results	Store all triplets
nums.sort()	Sort array	Enable two-pointer technique
for i, a in enumerate(nums)	Loop through each element	First number of triplet
if a > 0: break	Stop if positive	No valid triplets with positive first
if i>0 and a==nums[i-1]: continue	Skip duplicates	Avoid duplicate triplets
l, r = i+1, len(nums)-1	Set two pointers	Find pairs summing to -a
while l < r:	Loop until pointers cross	Check all pairs
threeSum = a + nums[l] + nums[r]	Calculate sum	Check if zero
if threeSum > 0: r -= 1	Sum too big	Decrease sum
elif threeSum < 0: l += 1	Sum too small	Increase sum
else:	Sum is zero	Found a triplet
res.append([a, nums[l], nums[r]])	Add to results	Store the triplet
l += 1; r -= 1	Move pointers	Continue searching
Skip duplicates	Avoid duplicates	Prevent duplicate triplets
return res	Return results	All triplets found"""

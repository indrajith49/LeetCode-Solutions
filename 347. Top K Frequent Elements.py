class Solution:
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        
        result = []
        
        for num, freq in count.most_common(k):
            result.append(num)
            
        return result



|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||


----------------------------------------------CORE IDEA----------------------------------------------------------------
1. Count Frequencies
→ Use Counter(nums) to count how many times each number appears.

2. Create an Empty Min-Heap
→ heap = [] — this will store (freq, num) pairs.

3. Push into Heap
→ Loop through counter.items() and push (freq, num).
→ Important: Store as (freq, num) because the heap sorts by the first element (frequency).

4. Maintain Heap Size
→ If len(heap) > k, pop the smallest frequency (heapq.heappop(heap)).
→ This keeps only the k largest frequencies in the heap.

5. Extract the Numbers
→ Return only the numbers (not frequencies) using [num for freq, num in heap].


import heapq
from collections import Counter

class Solution:
    def top_k_frequent(self, nums, k):
        counter = Counter(nums)
        result = []

        for num, freq in counter.items():
            heapq.heappush(result, (num, freq))

            if len(result)>k:
                heapq.heappop(result )

        return [num for freq, num in result]

sol = Solution()
print(sol.top_k_frequent([1,1,1,2,2,3], 2))



Let's Break It Down Like Legos
Imagine heap looks like this:

python
heap = [(2, 2), (3, 1)]
What is (2, 2)?

The first 2 is the frequency (how many times it appeared).

The second 2 is the actual number.

What is (3, 1)?

The 3 is the frequency.

The 1 is the number.

Now, Here is How Python Reads That Line
python
[num for freq, num in heap]
Part	What it means
for freq, num in heap	"Go through each pair in heap. Call the first thing freq and the second thing num."
num	"I only want the num part. Ignore freq."
[ ... ]	"Put all those num parts into a new list."

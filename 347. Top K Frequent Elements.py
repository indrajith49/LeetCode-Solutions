class Solution:
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        
        result = []
        
        for num, freq in count.most_common(k):
            result.append(num)
            
        return result



|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

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

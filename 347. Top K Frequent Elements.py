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

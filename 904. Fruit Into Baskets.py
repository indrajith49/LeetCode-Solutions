from collections import defaultdict
from typing import List
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = defaultdict(int)
        left = 0
        max_fruits = 0

        for right in range(len(fruits)):
            fruit = fruits[right]
            count[fruit] += 1

            # more than two distinct fruit types → shrink left side
            while len(count) > 2:
                left_fruit = fruits[left]
                count[left_fruit] -= 1
                if count[left_fruit] == 0:
                    del count[left_fruit]
                left += 1

            window_size = right - left + 1
            max_fruits = max(max_fruits, window_size)

        return max_fruits

sol = Solution()
print(sol.totalFruit([1,2,1]))
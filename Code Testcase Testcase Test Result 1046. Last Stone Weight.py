class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap)>1:
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)

            if first!=second:
                cur = first-second
                heapq.heappush(heap, -cur)

        return -heap[0] if heap else 0
------------------------------------------------------------------------------------------------------------

1. Convert all weights to negative numbers
→ Because Python’s heapq is a min-heap (smallest first).
→ By storing negatives, the heaviest stone becomes the most negative number, so it sits at the top.

2. Heapify the list
→ Rearranges the list into a valid heap structure in O(n) time.

3. Loop while more than 1 stone remains
→ while len(heap) > 1:

Pop the two heaviest stones
→ a = -heapq.heappop(heap) (convert back to positive)
→ b = -heapq.heappop(heap)

4. Smash them
→ If a != b, calculate cur = a - b
→ Push -cur back into the heap (as negative)

5. After the loop, return the last stone
→ If heap is not empty, return -heap[0]
→ Else return 0

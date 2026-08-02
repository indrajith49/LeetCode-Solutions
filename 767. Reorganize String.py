------------------------------------------------CORE IDEA--------------------------------------------------
1. Count frequencies using a hash map (Counter).

2. Push all characters into a max-heap (using negative counts) so the most frequent character is always on top.

3. Pop the most frequent character, add it to the result string, and decrease its count by 1.

4. If there is a character waiting in prev (from the previous step), push it back into the heap so it can be used again.

5. If the popped character still has remaining count, store it in prev to prevent using it again immediately.

6. Repeat until the heap is empty and no character is waiting.

7. If at any point a character is waiting but the heap is empty, return "" (impossible).

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)

        prev = None
        res = ""
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""

            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None

            if cnt != 0:
                prev = [cnt, char]

        return res

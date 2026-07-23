
        ------------------------------------------CORE IDEA-------------------------------------------------
so the quick summary step by step 
1. Edge case 
2. we will make a heap and push a tuple of summation, i(loop through nums1), 0 bcz we will only use nums2[0]
3. after we are done with making the heap we have to run another while loop so that we can push the values of summation(bcz heap is in ascending order), i and j so that we can append in the result(which is eventually our main array where we are gonna store the result)
4. then for further exploration we will increment j till the len(nums2) and then push to the heap summation of nums1[i] and nums2[j] and i and j+1  
5. then we are gonna return the result


from typing import List
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []

        heap = []

        for i in range(min(k, len(nums1))):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

        result = []



        while heap and len(result)<k:
            sum_val, i, j = heapq.heappop(heap)

            result.append([nums1[i], nums2[j]])

            if j+1< len(nums2):# this part still isnt clear
                heapq.heappush(heap, (nums1[i]+ nums2[j+1], i, j+1)) #this part still isnt clear

        return result

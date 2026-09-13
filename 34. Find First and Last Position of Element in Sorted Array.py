class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeft():
            l, r = 0, len(nums)-1
            left_ind = -1

            while l<=r:
                mid = (l+r)//2
                if nums[mid] == target:
                    left_ind = mid
                    r = mid-1

                elif nums[mid] < target:
                    l = mid+1

                else:
                    r = mid-1

            return left_ind


        def findRight():
            l, r = 0, len(nums)-1
            right_ind = -1
            while l<=r:
                mid = (l+r)//2
                if nums[mid] == target:
                    right_ind = mid
                    l = mid+1
                elif nums[mid] < target:
                    l = mid+1
                else:
                    r = mid-1

            return right_ind

        first = findLeft()
        last = findRight()
        return [first, last]
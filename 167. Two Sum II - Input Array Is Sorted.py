class Solution:
    def twosum(self, numbers, target):
        l, r = 0, len(numbers)-1

        while l<r:
            current_sum = numbers[l] + numbers[r]

            if current_sum == target:
                return [l+1, r+1]

            if current_sum<target:
                l+=1
            else:
                r-=1


sol = Solution()
print(sol.twosum([2,7,11,15], 9))

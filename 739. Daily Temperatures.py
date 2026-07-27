---------------------------------------------------CORE IDEA--------------------------------------------
We store indices in a stack. 
As long as the stack is not empty and the current temperature is greater than the temperature at the top index of the stack, 
we pop that index, subtract it from the current index to get the number of days waited, 
and store it in the answer array. After resolving all cooler days, we push the current index onto the stack. 
Finally, we return the answer array.
-----------------------------------------------------BRUTE FORCE-----------------------------------------------------

class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        answer = [0]*n
        for i in range(n):
            for j in range(i+1, n):
                if temperatures[j]>temperatures[i]:
                    answer[i] = j-i
                    break
        return answer

sol = Solution()
print(sol.dailyTemperatures([73,74,75,71,69,72,76,73]))

------------------------------------------------------------------------------------------------------------------------

------------------------------------------------------STACK & QUEUE------------------------------------------------------
class Solution:
    def dailyTemperatures(self, temperatures):

        n = len(temperatures)
        result = [0] * n
        stack = []
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                previous_index = stack.pop()
                result[previous_index] = i-previous_index
            stack.append(i)
        return result

sol = Solution()
print(sol.dailyTemperatures([73,74,75,71,69,72,76,73]))


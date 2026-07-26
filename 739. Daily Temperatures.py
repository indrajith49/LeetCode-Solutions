---------------------------------------------------CORE IDEA--------------------------------------------




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


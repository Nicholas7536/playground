class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        t = 0

        for t in range(len(temperatures)):

            while stack and temperatures[t] > temperatures[stack[-1]]:
                
                idx = stack.pop()
                res[idx] = t - idx

            stack.append(t)
        
        return res
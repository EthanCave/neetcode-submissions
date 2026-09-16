class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #brute force solution
        # solution = []
        # for i in range(len(temperatures)):
        #     for j in range(i,len(temperatures)):

        #         if temperatures[j] > temperatures[i]:
        #             solution.append(j-i)
        #             break

        #     if len(solution) <= i:
        #         solution.append(0)

        # return solution

        solution = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                j = stack.pop()
                solution[j] = i - j
            stack.append(i)
        return solution









            
        


        
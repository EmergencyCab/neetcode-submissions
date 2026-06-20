class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n #Create an output array with zeros. [0,0,0,0,0,0,0].

        for i in range(n):
            for j in range(i+1, n):
                if temperatures[j] > temperatures[i]:
                    result[i] = j - i #Store that as the answer for day i.
                    break 
        return result 
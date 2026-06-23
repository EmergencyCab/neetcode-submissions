class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if intervals == []:
            return []

        result = []
        intervals.sort()

        #When to add? if empty or if last thing i added is less than 
        #whats coming e.g: (x,3) < (y,6) -> 6 already covers 3

        #interval[0] -> start time of interval
        #interval[1] -> end time of interval

        for interval in intervals:
            if result == [] or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1]) 
        return result 
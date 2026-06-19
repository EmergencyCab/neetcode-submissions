class Solution:
    def maxArea(self, heights: List[int]) -> int:
        beg = 0 
        end = len(heights) - 1
        max_area = 0
        while beg < end: 
            max_area = max(max_area, min(heights[beg], heights[end])*(end - beg))
            if heights[beg] >= heights[end]:
                end -= 1
            else:
                beg +=1 
        return max_area


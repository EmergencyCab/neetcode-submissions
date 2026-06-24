class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0] #first index
        curr_sum = 0 #there is nothing right now 
        for num in nums:
            curr_sum = max(curr_sum+num, num)
            max_sum = max(max_sum, curr_sum)
        return max_sum
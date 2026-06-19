class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()

        #Now set the a value to be every single numbers in num 
        #[-2,0,2, -2, 0]
        # a  l        r
        for i in range(len(nums)):
            #cant have duplicates after the first round guys
            if i !=  0 and nums[i] == nums[i-1]:
                continue
            #2 sum on the remainder of the list 
            l = i+1
            r = len(nums) - 1
            while l < r:
                total = nums[i]+nums[l]+nums[r]
                if total > 0: 
                    r -= 1 
                elif total < 0:
                    l += 1
                else: 
                    ret.append([nums[i], nums[l], nums[r]])
                    l += 1
                    #preventing duplicates, cant have same value as before
                    #[-2,-2,0,0,2]
                    #  a       l r 
                    while l < r and nums[l] == nums[l-1]: 
                        l+=1
        return ret

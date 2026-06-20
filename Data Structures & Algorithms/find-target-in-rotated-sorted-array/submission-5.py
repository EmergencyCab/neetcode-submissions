class Solution:
    def search(self, nums: List[int], target: int) -> int:
        beg, end = 0, len(nums) -1 

        while beg < end:
            mid = (beg + end) // 2

            if nums[mid] == target: 
                return mid
            
            #now check which half is sorted and see target is inside
            # see which half is sorted (for left)
            if nums[beg] <= nums[mid]:
                  #b     m  e
                #[3,4,5,6,1,2], target = 1
                       #e
                if nums[beg] <= target <= nums[mid]:
                    end = mid - 1
                else: 
                    beg = mid + 1

            else: 
                #[3,4,5,6,1,2], target = 1
                # b     m    e
                         #b
                if nums[mid] <= target <= nums[end]:
                    beg = mid + 1
                else:
                    end = mid - 1
                
        return -1 if nums[end] != target else end
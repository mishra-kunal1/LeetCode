class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        local_max=1
        global_max=1
        for i in range(1,len(nums)):
            if(nums[i]>nums[i-1]):
                local_max=local_max+1
            else:
                local_max=1
            global_max=max(local_max,global_max)
            
        return global_max
        
        
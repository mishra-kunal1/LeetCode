class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if(len(nums)==0):
            return []
        temp=[0]*len(nums)
        index=len(nums)-1
        i=0
        j=len(nums)-1
        for ele in nums:
            if(nums[i]*nums[i]>nums[j]*nums[j]):
                
                temp[index]=nums[i]*nums[i]
                i=i+1
                index=index-1
            else:
                
                temp[index]=nums[j]*nums[j]
                j=j-1
                index=index-1
        return temp
                
                
            
            
        
        
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if(len(nums)==0):
            return []
        temp=[0]*len(nums)
        index=len(nums)-1
        i=0
        j=len(nums)-1
        for ele in nums:
            left_square=nums[i]*nums[i]
            right_square=nums[j]*nums[j]
            if(left_square>right_square):
                
                temp[index]=left_square
                i=i+1
                index=index-1
            else:
                
                temp[index]=right_square
                j=j-1
                index=index-1
        return temp
                
                
            
            
        
        
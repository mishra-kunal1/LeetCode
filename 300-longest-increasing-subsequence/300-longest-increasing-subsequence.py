class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis=[1]*len(nums)
        n=len(nums)
        for i in range(1,n):
            j=i-1
            while(j>=0):
                if(nums[j]<nums[i]):
                    possibleAns=lis[j]+1
                    lis[i]=max(lis[i],possibleAns)
                    j=j-1
                else:
                    j=j-1
                    continue
        max_len=1
        for k in range(len(lis)):
            if(lis[k]>max_len):
                max_len=lis[k]
        return max_len
            
        
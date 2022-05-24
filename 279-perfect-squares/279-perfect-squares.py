class Solution:
    def min_squares_req(self,n,dp):
        if(n==0):
            return 0
        min_val=10000

        for i in range(1,int(math.sqrt(n))+1):
            if(dp[n-i*i]==-1):
                ans=self.min_squares_req(n-i*i,dp)
                dp[n-i*i]=ans
            else:
                ans=dp[n-i*i]
            min_val=min(ans,min_val)
        return 1+min_val
    def numSquares(self, n: int) -> int:
        
        dp=[-1 for i in range (n+1)]
        ans=self.min_squares_req(n,dp)
        return ans
        
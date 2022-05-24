class Solution:
    def fib_helper(self,n,dp):
        if n==0 or n==1:
            return n
        if dp[n-1]==-1:
            ans1=self.fib_helper(n-1,dp)
            dp[n-1]=ans1
        else:
            ans1=dp[n-1]
        if dp[n-2]==-1:
            ans2=self.fib_helper(n-2,dp)
            dp[n-2]=ans2
        else:
            ans2=dp[n-2]
        return (ans1+ans2)
        
        
        
    def fib(self, n: int) -> int:
        dp=[-1 for i in range(n+1)]
        ans=self.fib_helper(n,dp)
        return ans
        
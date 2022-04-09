class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n==1):
            return 1
        if(n==2):
            return 2
        if(n>2):
            count_arr=[0]*(n+1)
            count_arr[1]=1
            count_arr[2]=2
            for i in range(3,n+1):
                count_arr[i]=count_arr[i-1]+count_arr[i-2]
        return count_arr[n]
        
        
        
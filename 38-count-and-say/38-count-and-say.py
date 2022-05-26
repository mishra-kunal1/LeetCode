class Solution:
        
    def countAndSay(self, n: int) -> str:
        if(n==1):
            return "1"
        res=self.countAndSay(n-1)
        final_string=""
        freq=0
        for i in range(len(res)):
            freq=freq+1
            if(i==len(res)-1 or res[i]!=res[i+1]):
                final_string+=str(freq)+res[i]
                freq=0
        return final_string
       
        
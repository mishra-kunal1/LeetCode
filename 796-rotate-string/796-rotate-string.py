class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        if(len(s)!=len(goal)):
            return False
        final_string=s+s
        if(final_string.find(goal)!=-1):
            return True
        else:
            return False
        
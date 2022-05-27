class Solution:
       def lengthOfLongestSubstring(self,string: str) -> int:
        max_len=256
        max_seq=0
        
        for i in range(len(string)):

            is_visited=[False]*max_len 
            #is_visited[ord(string[i])-ord('a')]=True
            for j in range(i+1,len(string)+1):
                if(is_visited[ord(string[j-1])-ord('a')])==True:
                    break
                else:
                    is_visited[ord(string[j-1])-ord('a')]=True
                    max_seq=max(max_seq,j-i)

        return max_seq 
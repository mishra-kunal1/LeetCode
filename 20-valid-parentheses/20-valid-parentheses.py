class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        char_list=[]  #stack
        for index,char in enumerate(s):
            char_list.append(char)
            if(len(char_list)!=0 and len(char_list)!=1 ):
                if((char_list[-1]=='}' and char_list[-2]=='{') or (char_list[-1]==')' and char_list[-2]=='(') or (char_list[-1]==']' and char_list[-2]=='[')):
                    char_list.pop(-1)
                    char_list.pop(-1)
        if(len(char_list)==0):
            return True
        else:
            return False
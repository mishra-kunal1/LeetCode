class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mydict={}
        for index,ele in enumerate(nums):
            if target-ele in mydict:
                return(mydict[target-ele],index)
            else:
                mydict[ele]=index
                
        
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if(list1 is None):
            return list2
        if(list2 is None):
            return list1
        
        
        if(list1.val>list2.val):
            head=list2
            list2=list2.next
        else:
            head=list1
            list1=list1.next
            
        curr=head
        
        while(list1 and list2):
            dum=None
            if(list1.val>list2.val):
                dum=list2
                list2=list2.next
            else:
                dum=list1
                list1=list1.next
            curr.next=dum
            curr=dum
            
        if(list1):
            curr.next=list1
        if(list2):
            curr.next=list2
        return head
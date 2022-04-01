# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def ll_to_num(self,head):
        power=0
        sum=0
        while(head is not None):
            place_val=(head.val)*(10**power)
            sum=sum+place_val
            head=head.next
            power=power+1
        return sum
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num_1=Solution().ll_to_num(l1)
        num_2=Solution().ll_to_num(l2)
        res=num_1+num_2
        s=str(res)
        head=None
        curr=head
        for digit in s[::-1]:
            if head is None:
                head= ListNode(digit)
            else:
                curr=head
                while(curr.next is not None):
                    curr=curr.next
                curr.next=ListNode(digit)
        return head
            
            
            
        
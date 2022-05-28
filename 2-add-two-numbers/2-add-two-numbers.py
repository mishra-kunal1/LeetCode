# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def print_ll(self,head):
        while(head):
            print(head.val,end="")
            head=head.next
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3=ListNode(0)
        curr=l3
        carry=0
        while(l1 or l2):
            if(l1 is None):
                val1=0
            else:
                val1=l1.val
            if(l2 is None):
                val2=0
            else:
                val2=l2.val
            sum_val=val1+val2+carry
            carry=sum_val//10
            curr.next=ListNode(sum_val%10)
            
            curr=curr.next
            if(l1):
                l1=l1.next
            if(l2):
                l2=l2.next
        if(carry>0):
            curr.next=ListNode(carry)
        return l3.next
            
            
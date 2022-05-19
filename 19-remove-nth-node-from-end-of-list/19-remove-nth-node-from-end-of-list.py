# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def find_length(self,head):
        count=0
        while(head is not None):
            head=head.next
            count+=1
        return count
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if head is None:
            return
        
        total=self.find_length(head)
        if(total==1):
            return None
        
        val=total-n+1
        if(val==1):
            return head.next
        curr=head
        prev=head
        
        while(val!=1):
            prev=curr
            curr=curr.next
            val=val-1
        prev.next=curr.next
        return head
        
        
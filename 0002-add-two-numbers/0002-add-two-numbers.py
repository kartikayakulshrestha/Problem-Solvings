# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverseMyList(l):
            curr=l
            prev=None
            while curr:
                
                temp=curr
                p=curr.next
                curr.next=prev
                prev=temp
                curr=p
            return prev
        
        list1=l1
        list2=l2
        curr1=list1
        curr2=list2
        prev1=prev2=prev=None
        dummy=ListNode(-1)
        prev=dummy
        carry=0
        while curr1 and curr2:
            value=curr1.val+curr2.val+carry
            if value>9:
                value%=10
                carry=1
            else:
                carry=0
            
            curr=ListNode(value)
            prev.next=curr
            prev=curr
            

            curr1=curr1.next
            curr2=curr2.next
        while curr1:
            value=curr1.val+carry
            if value>9:
                value%=10
                carry=1
            else:
                carry=0
            
            curr=ListNode(value)
            prev.next=curr
            prev=curr

            curr1=curr1.next
        while curr2:
            value=curr2.val+carry
            if value>9:
                value%=10
                carry=1
            else:
                carry=0
            
            curr=ListNode(value)
            prev.next=curr
            prev=curr
            

            curr2=curr2.next
        
        if carry:
            curr=ListNode(1)
            prev.next=curr
            prev=curr    
            carry=0
        
        
        return dummy.next
        

            
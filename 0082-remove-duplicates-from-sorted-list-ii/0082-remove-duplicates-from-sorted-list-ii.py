# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dic={}
        curr=head
        while curr:
            if curr.val not in dic:
                dic[curr.val]=1
            else:
                dic[curr.val]=0
            curr=curr.next
        if len(dic)==0:
            return None
        temp=ListNode()
        temp1=temp
        for i,j in dic.items():
            if j:
                x=ListNode(i)
                temp1.next=x
                temp1=temp1.next
        temp=temp.next
        return temp
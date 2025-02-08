# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        temphead=head.next
        prevhead=head

        while temphead:
            if temphead.val==prevhead.val:
                temphead=temphead.next
            else:
                prevhead.next=temphead
                prevhead=temphead
                temphead=temphead.next
        prevhead.next=temphead
        return head
        
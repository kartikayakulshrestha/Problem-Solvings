# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        newlist=ListNode(0)
        temp=newlist
        while 1:
            count=0
            
            smallestIndex=float("inf")
            smaller=float("inf")
            for index,linkedlist in enumerate(lists):
                
                if not linkedlist:
                    count+=1
                else:
                    
                    if linkedlist.val<smaller:
                        smallestIndex=index
                        smaller=linkedlist.val

            if count==len(lists):
                newlist=newlist.next
                return newlist
            temp.next=ListNode(lists[smallestIndex].val)
            temp=temp.next
            
            lists[smallestIndex]=lists[smallestIndex].next
            
        return None
        
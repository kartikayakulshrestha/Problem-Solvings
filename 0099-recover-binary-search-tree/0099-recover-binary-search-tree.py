# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        l=[]
        
        curr=root
        stack=[]
        while curr or stack:
            while curr:
                stack.append(curr)
                curr=curr.left
            curr=stack.pop()
            l.append(curr)
            curr=curr.right

        val=[n.val for n in l]
        val.sort()
        
        for i in range(len(l)):
            l[i].val=val[i]
            
        
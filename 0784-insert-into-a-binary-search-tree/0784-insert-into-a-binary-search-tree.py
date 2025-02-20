# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        x=root 
        if not x:
            return TreeNode(val)
        while x:
            if not x.left and not x.right:
                if val<x.val:
                    x.left=TreeNode(val)
                else:
                    x.right=TreeNode(val)
                break
            
            elif x.val<val:
                if not x.right:
                    x.right=TreeNode(val)
                    break
                x=x.right
            elif x.val>val:
                if not x.left:
                    x.left=TreeNode(val)
                    break
                x=x.left
        return root
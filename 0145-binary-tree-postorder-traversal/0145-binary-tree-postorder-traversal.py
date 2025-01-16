# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        post=[]
        stack=[root]
        if not root:
            return []
        while stack:
            x=stack.pop()
            post.append(x.val)
            if x.left:
                stack.append(x.left)
            if x.right:
                stack.append(x.right)
        return post[::-1]
        
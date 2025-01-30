# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        curr=root 
        stack=[]
        visited=set()
        ans=[]
        while curr or stack:
            while curr:
                stack.append(curr)
                curr=curr.left
            curr=stack.pop()
            if curr.val in visited:
                return False
            ans.append(curr.val)
            visited.add(curr.val)
            curr=curr.right
        for i in range(len(ans)-1):
            if ans[i]>ans[i+1]:
                return False
        return True
        
        
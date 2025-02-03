class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        stack=[]
        ans=[]
        for i in range(n-1,-1,-1):
            if not stack:
                ans.append(n-1)
                
            else:
                while stack and heights[stack[-1]]>=heights[i]:
                    stack.pop()
                if stack:
                    ans.append(stack[-1]-1)
                else:
                    ans.append(n-1)
                
            stack.append(i)
        ans=ans[::-1]
        peeche=[]
        stack=[]
        for i in range(n):
            if not stack:
                peeche.append(0)
            else:
                while stack and heights[stack[-1]]>=heights[i]:
                    stack.pop()
                if stack:
                    peeche.append(stack[-1]+1)
                else:
                    peeche.append(0)
            stack.append(i)
        
        maxi=0
        for i in range(n):
            maxi=max(heights[i]*(ans[i]-peeche[i]+1),maxi)
        return maxi
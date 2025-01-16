class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        stack=[]
        n=len(prices)
        for i in range(n-1,-1,-1):
            if not stack:
                ans=max(ans,0)
                stack.append(prices[i])
            else:
                while stack and stack[-1]<prices[i]:
                    stack.pop()
                if not stack:
                    ans=max(ans,0)
                    stack.append(prices[i])
                else:
                    ans=max(ans,stack[-1]-prices[i])
                    if prices[i]>stack[-1]:
                        stack.append(prices[i])
          
        return ans
        
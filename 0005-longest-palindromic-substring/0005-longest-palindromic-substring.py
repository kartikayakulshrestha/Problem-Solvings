class Solution:
    def longestPalindrome(self, s: str) -> str:
        # time complexity o(n^2)
        n=len(s)
        ans=[]
        
        for i in range(n):
            for j in range(i,n):
                ans.append(s[i:j+1])
        ans.sort(key=len)
        for i in range(len(ans)-1,-1,-1):
            if ans[i]==ans[i][::-1]:
                return ans[i]
        return ""

                    
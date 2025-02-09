class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n,m,q=len(s1),len(s2),len(s3)
        if n+m!=q:
            return False
        memo={}
        def recur(i,j,k):
            if k==q:
                if i==n and j==m:
                    return True
                else:
                    return False
            if (i,j) in memo:
                return memo[(i,j)]
            if i<n and s1[i]==s3[k]:
                if recur(i+1,j,k+1):
                    memo[(i,j)]=True
                    return True
            if j<m and s2[j]==s3[k]:
                if recur(i,j+1,k+1):
                    memo[(i,j)]=True
                    return True
            memo[(i,j)]=False
            return False

        return recur(0,0,0)
    

        
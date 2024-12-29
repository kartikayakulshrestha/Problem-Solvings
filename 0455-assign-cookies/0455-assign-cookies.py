class Solution:
    def findContentChildren(self, s: List[int], coo: List[int]) -> int:
        s.sort()
        coo.sort()
        n,m=len(s),len(coo)
        i,j=0,0
        c=0
        while i<n and j<m:

            if s[i]<=coo[j]:
                c+=1
                i+=1
                j+=1
            else:
                j+=1
        return c
        
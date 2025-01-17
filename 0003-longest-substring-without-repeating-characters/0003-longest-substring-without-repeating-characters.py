from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        sets=set()
        n=len(s)
        m=0
        while r<n and l<n:

            if s[r] not in sets:
                sets.add(s[r])
                r+=1
            else:
                
                sets.remove(s[l])
                l+=1
            m=max(m,r-l)
        return m
                

        
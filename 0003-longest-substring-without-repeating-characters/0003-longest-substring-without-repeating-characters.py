class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen=0
        n=len(s)
        i=0
        j=0
        visited=set()
        while j<n:
            if s[j] not in visited:
                visited.add(s[j])
                j+=1
            else:
                maxLen=max(j-i,maxLen)
                
                while s[j] in visited:
                    visited.remove(s[i])
                    i+=1
                visited.add(s[j])
                j+=1
            
        maxLen=max(j-i,maxLen)
        return maxLen  
            
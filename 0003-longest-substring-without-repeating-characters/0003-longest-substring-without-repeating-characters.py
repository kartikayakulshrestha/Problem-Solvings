class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        visited=set()
        i=0
        j=0
        n=len(s)
        max_len=-1
        while j<n:
            if s[j] not in visited:
                visited.add(s[j])
                j+=1
            else:
                max_len=max(max_len,j-i)
                while i<j and s[i]!=s[j]:
                    visited.remove(s[i])
                    i+=1
                visited.remove(s[i])
                i+=1
                visited.add(s[j])
                j+=1
        max_len=max(max_len,j-i)
        return max_len

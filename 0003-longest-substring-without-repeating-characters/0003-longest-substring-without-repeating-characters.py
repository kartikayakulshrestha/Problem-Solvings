class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #basic way is to create all possible substrings and then check what to do
        sets=set()
        n=len(s)

        max_len=0
        j=i=0
        while j<n:
            
            if s[j] not in sets:
                sets.add(s[j])
                
                j+=1
            else:
                max_len=max(max_len,j-i)
                while i<j and s[i]!=s[j]:
                    sets.remove(s[i])
                    i+=1
                sets.remove(s[i])
                i+=1
                sets.add(s[j])
                j+=1

            
        max_len=max(max_len,j-i)    
        return max_len

        
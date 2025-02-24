class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        x = strs[0]  # Initialize prefix with the first string
        
        for i in range(1, len(strs)):  # Start from the second string
            j = 0
            while j < len(x) and j < len(strs[i]) and strs[i][j] == x[j]:
                j += 1
            x = x[:j]  # Update prefix to matched portion
            
            if not x:  # If prefix becomes empty, return immediately
                return ""
        
        return x
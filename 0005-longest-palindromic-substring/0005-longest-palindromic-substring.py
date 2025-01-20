class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp=[[False]*n for i in range(n)]
        start, max_len = 0, 0

        # Fill the DP table
        for length in range(1, n + 1):  # Length of the substring
            for i in range(n - length + 1):
                j = i + length - 1  # Ending index of the substring
                
                if length == 1:
                    dp[i][j] = True  # Single character
                elif length == 2:
                    dp[i][j] = (s[i] == s[j])  # Two characters
                else:
                    dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]  # More than two characters
                
                # Update the longest palindrome if this substring is valid
                if dp[i][j] and length > max_len:
                    start, max_len = i, length
        
        # Return the longest palindrome substring
        return s[start:start + max_len]

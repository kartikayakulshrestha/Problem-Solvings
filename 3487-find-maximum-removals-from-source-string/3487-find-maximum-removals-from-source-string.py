class Solution:
    def maxRemovals(self, source: str, pattern: str, t: List[int]) -> int:
        n = len(source)
        m = len(pattern)
        dp = [float('inf')] * (m + 1)
        dp[0] = 0
        isTarget = [False] * n
        for idx in t:
            isTarget[idx] = True
        
        for i in range(n):
            for j in range(m, 0, -1):
                if source[i] == pattern[j-1] and dp[j-1] != float('inf'):
                    dp[j] = min(dp[j], dp[j-1] + (1 if isTarget[i] else 0))
        
        return len(t) - (0 if dp[m] == float('inf') else dp[m])


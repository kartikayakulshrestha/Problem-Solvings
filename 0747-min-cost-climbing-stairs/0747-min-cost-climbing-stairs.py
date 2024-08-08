class Solution:
    def f(self, n, arr, dp):
        
        if dp[n] != -1:  # Check if the result for step `n` is already computed
            return dp[n]  # Return the already computed minimum cost for step `n`
        if n == 0:  # Base case for the first step
            return arr[0]
        elif n == 1:  # Base case for the second step
            return arr[1]
        
        # Recursive case: compute the minimum cost to reach step `n`
        left = self.f(n-1, arr, dp)
        right = self.f(n-2, arr, dp)
        
        
        dp[n] = min(left, right) + arr[n]  # Store the result in dp[n]
        return dp[n]  # Return the computed minimum cost for step `n`
    
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 1:  # Edge case: only one step
            return cost[0]
        if len(cost) == 2:  # Edge case: two steps
            return min(cost)
        
        dp = [-1] * len(cost)  # Initialize dp array with -1
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        # Compute the minimum cost to reach the last step or second to last step
        return min(self.f(len(cost) - 1, cost, dp), self.f(len(cost) - 2, cost, dp))

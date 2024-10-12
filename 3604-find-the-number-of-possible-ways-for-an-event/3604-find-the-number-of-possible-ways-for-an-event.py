class Solution:
    def numberOfWays(self, n: int, x: int, y: int) -> int:
        MOD = 10**9 + 7
        
        def generate_combinations(limit: int) -> list:
            combinations = [[0] * (limit + 1) for _ in range(limit + 1)]
            for i in range(limit + 1):
                combinations[i][0] = 1
                for j in range(1, i + 1):
                    combinations[i][j] = (combinations[i - 1][j - 1] + combinations[i - 1][j]) % MOD
            return combinations
        
        def generate_stirling_numbers(n: int, x: int) -> list:
            stirling = [[0] * (x + 1) for _ in range(n + 1)]
            stirling[0][0] = 1
            for i in range(1, n + 1):
                for j in range(1, x + 1):
                    stirling[i][j] = (j * stirling[i - 1][j] + stirling[i - 1][j - 1]) % MOD
            return stirling
        
        def generate_factorials(limit: int) -> list:
            factorials = [1] * (limit + 1)
            for i in range(1, limit + 1):
                factorials[i] = factorials[i - 1] * i % MOD
            return factorials
        
        C = generate_combinations(x)
        S = generate_stirling_numbers(n, x)
        fact = generate_factorials(x)
        
        total = 0
        for k in range(1, x + 1):
            power_y_k = pow(y, k, MOD)
            contribution = (C[x][k] * S[n][k] % MOD * fact[k] % MOD * power_y_k % MOD) % MOD
            total = (total + contribution) % MOD
        
        return total
class Solution:
    def countPrimes(self, n: int) -> int:
        primes=[0]*(n+1)
        for i in range(2,n+1):
            for j in range(i*i,n+1,i):
                primes[j]=1
        count=0
        for i in range(2,n):
            
            if primes[i]==0:
                
                count+=1
        return count
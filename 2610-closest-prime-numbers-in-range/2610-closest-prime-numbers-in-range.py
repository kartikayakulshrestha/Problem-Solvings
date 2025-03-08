class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        n=right
        primes=[1]*(right+1)
        primes[0]=primes[1]=0
        for i in range(2,n+1):
            if primes[i]:
                
                for j in range(i*i,n+1,i):
                    
                    primes[j]=0
        l=[]
        for i in range(left,right+1):
            if primes[i]:
                l.append(i)
        mini=float("inf")
        tt=[-1,-1]
        for i in range(len(l)-1):
            p=l[i+1]-l[i]
            if p<mini:
                mini=p
                tt[0]=l[i]
                tt[1]=l[i+1]
        return tt
        
        
        
        

        
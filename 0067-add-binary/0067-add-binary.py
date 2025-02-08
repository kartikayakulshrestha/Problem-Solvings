class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a)<len(b):
            b,a=a,b
        n=len(a)
        m=len(b)
        i=n-1
        j=m-1
        carry=0
        ans=""
        for k in range(min(n,m)):
            if a[i]=="1" and b[j]=="1":
                if carry:
                    ans+="1"
                else:
                    ans+="0"
                    carry=1
            elif a[i]=="1" or b[j]=="1":
                if carry:
                    ans+="0"
                else:
                    ans+="1"
            else:
                if carry:
                    ans+="1"
                    carry=0
                else:
                    ans+="0"
            i-=1
            j-=1
        
        while i>=0 and carry:
            if a[i]=="1" and carry:
                
                ans+="0"
                carry=1
                
            elif a[i]=="0" and carry:
                ans+="1"
                carry=0
            i-=1
        while i>=0:
            ans+=a[i]
            i-=1
        if carry:
            ans+="1"   
        return ans[::-1]
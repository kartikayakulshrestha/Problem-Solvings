class Solution:
    def subArrayRanges(self, arr: List[int]) -> int:
        n=len(arr)
        def nse(arr):
            stack=[]
            ans=[]
            for i in range(n-1,-1,-1):
                if len(stack):
                    while len(stack) and stack[-1][0]>arr[i]:
                        stack.pop()
                    if len(stack):
                        ans.append(stack[-1][1])
                    else:
                        ans.append(n)
                    stack.append([arr[i],i])
                else:
                    ans.append(n)
                    stack.append([arr[i],i])
            return ans[::-1]
        def nle(arr):
            stack=[]
            ans=[]
            for i in range(n-1,-1,-1):
                if len(stack):
                    while len(stack) and stack[-1][0]<=arr[i]:
                        stack.pop()
                    if len(stack):
                        ans.append(stack[-1][1])
                    else:
                        ans.append(n)
                    stack.append([arr[i],i])
                else:
                    ans.append(n)
                    stack.append([arr[i],i])
            return ans[::-1]
        def pse(arr):
            stack=[]
            ans=[]
            for i in range(n):
                if len(stack):
                    while len(stack) and stack[-1][0]>=arr[i]:
                        stack.pop()
                    if len(stack):
                        ans.append(stack[-1][1])
                    else:
                        ans.append(-1)
                    stack.append([arr[i],i])
                else:
                    ans.append(-1)
                    stack.append([arr[i],i])
            return ans
        def ple(arr):
            stack=[]
            ans=[]
            for i in range(n):
                if len(stack):
                    while len(stack) and stack[-1][0]<arr[i]:
                        stack.pop()
                    if len(stack):
                        ans.append(stack[-1][1])
                    else:
                        ans.append(-1)
                    stack.append([arr[i],i])
                else:
                    ans.append(-1)
                    stack.append([arr[i],i])
            return ans
        
        s1,l1,s2,l2=nse(arr),nle(arr),pse(arr),ple(arr)
        total=0
        for i in range(n):
            x=(s1[i]-i)*(i-s2[i])
            y=(l1[i]-i)*(i-l2[i])
            total+=(y*arr[i])-(x*arr[i])
        return total
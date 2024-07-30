class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==1:
            return [[nums[0]]]
        elif len(nums)==2:
            return [[nums[0],nums[1]],[nums[1],nums[0]]]
        elif len(nums)==3:
            l=[]
            for i in nums:
                for j in nums:
                    if i==j:
                        continue
                    for k in nums:
                        if i==j or j==k or i==k:
                            continue

                        l.append([i,j,k])
        
            return l
        elif len(nums)==4:
            l=[]
            for i in nums:
                for j in nums:
                    if i==j:
                        continue
                    for k in nums:
                        if i==j or j==k or i==k:
                            continue
                        for n in nums:
                            if i==n or j==n or k==n:
                                continue
                            
                            l.append([i,j,k,n])
            return l
        elif len(nums)==5:
            l=[]
            for i in nums:
                for j in nums:
                    if i==j:
                        continue
                    for k in nums:
                        if i==j or j==k or i==k:
                            continue
                        for n in nums:
                            if i==n or j==n or k==n:
                                continue
                            
                            for m in nums:
                                if m==i or j==m or k==m or n==m:
                                    continue
                                l.append([i,j,k,n,m])

            return l
        if len(nums)==6:
            l=[]
            for i in nums:
                for j in nums:
                    if i==j:
                        continue
                    for k in nums:
                        if i==j or j==k or i==k:
                            continue
                        for n in nums:
                            if i==n or j==n or k==n:
                                continue
                            
                            for m in nums:
                                if m==i or j==m or k==m or n==m:
                                    continue
                                for b in nums:
                                    if b==i or j==b or k==b or n==b or b==m:
                                        continue

                                    l.append([i,j,k,n,m,b])
                                
            return l
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        if n>=3 and nums[0]==0 and nums[-1]==0:
            return [[0,0,0]]
        visited=set()
        ans=[]
        for i in range(n-2):
            l=i+1
            r=n-1
            while l<r:
                x=(nums[i],nums[l],nums[r])
                q=[nums[i],nums[l],nums[r]]
                p=nums[i]+nums[l]+nums[r]
                if p==0:
                    if x not in visited:
                        visited.add(x)
                        ans.append(q)
                    l+=1
                    r-=1
                elif p<0:
                    l+=1
                elif p>0:
                    r-=1
        return ans
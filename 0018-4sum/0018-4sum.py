class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        seen=set()
        ans=[]
        nums.sort()
        for i in range(n):
            for j in range(i+1,n):
                l=j+1
                r=n-1
                while l<r:
                    p=[nums[i],nums[j],nums[l],nums[r]]
                    v=(nums[i],nums[j],nums[l],nums[r])
                    x=sum(p)
                    if x==target:
                        if v not in seen:
                            ans.append(p)
                        seen.add(v)
                        l+=1
                        r-=1
                    elif x<target:
                        l+=1
                    else:
                        r-=1
        return ans 


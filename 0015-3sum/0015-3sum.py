class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
    
        n=len(nums)
        done=set()
        for i in range(n):
            
            l=i+1
            r=n-1
            while l<r:
                    
                p=nums[l]+nums[r]+nums[i]
                v=(nums[i],nums[l],nums[r])
                    
                if p==0:
                    if v not in done:
                        ans.append([nums[i],nums[l],nums[r]])
                    done.add(v)
                    l+=1
                    r-=1
                elif p<0:
                    l+=1
                else:
                    r-=1
        return ans
                
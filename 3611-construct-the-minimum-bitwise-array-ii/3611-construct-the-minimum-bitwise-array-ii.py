class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        
        for i in range(n):
            num = nums[i]
            minimal_ans = float('inf')
            found = False
            
            
            for bit in range(31):
                if ((num >> bit) & 1) == 1:
                    
                    candidate = num & ~(1 << bit)
                    
                    
                    if candidate < 0:
                        continue
                    
                    
                    if (candidate | (candidate + 1)) == num:
                        if candidate < minimal_ans:
                            minimal_ans = candidate
                            found = True
            
            if found:
                ans[i] = minimal_ans
            else:
                ans[i] = -1
        
        return ans
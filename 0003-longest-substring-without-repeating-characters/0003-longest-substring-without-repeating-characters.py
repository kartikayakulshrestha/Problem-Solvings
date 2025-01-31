from collections import OrderedDict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ord=OrderedDict()
        maxLen=1
        if s=="":
            return 0
        for i in s:
            if i not in ord:
                ord[i]=1
            else:
                maxLen=max(maxLen,len(ord))
                
                x=ord.popitem(last=False)
                
                while ord and x[0]!=i:
                    x=ord.popitem(last=False)
                ord[i]=1
            
        maxLen=max(maxLen,len(ord))    
        return maxLen
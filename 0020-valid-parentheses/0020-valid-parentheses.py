class Solution:
    def isValid(self, s: str) -> bool:
        if s[0] in ")]}" or s[-1] in "([{":
            return False
        
        stack=[]
        i=0
        while i<len(s):
            if s[i] in "([{":
                stack.append(s[i])
                
            else:
                if stack and ( (s[i]==")" and stack[-1]=="(") or (s[i]=="]" and stack[-1]=="[") or (s[i]=="}" and stack[-1]=="{")):
                    stack.pop()
                else:
                    return False 
            i+=1

        return not stack
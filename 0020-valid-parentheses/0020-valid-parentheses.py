class Solution:
    def isValid(self, s: str) -> bool:
        n=len(s)
        if s[0] in ")}]":
            return False
        stack=[]
        for i in range(n):
            if s[i] in "({[":
                stack.append(s[i])
            else:
                if stack and ((stack[-1]=="{" and s[i]=="}") or (stack[-1]=="(" and s[i]==")") or (stack[-1]=="[" and s[i]=="]")):
                    stack.pop()
                else:
                    return False
        return False if len(stack) else True
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        dic={}
        n=len(words)
        for i in words[0]:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
            
        for i in range(1,n):
            dic1={}
            for j in words[i]:
                if j in dic1:
                    dic1[j]+=1
                else:
                    dic1[j]=1
            dic2=dic.copy()
            for k,j in dic2.items():
                if k not in dic1:
                    
                    dic.pop(k)
                else:
                    dic[k]=min(dic[k],dic1[k])
        m=[]
        for i,j in dic.items():
            m+=[i]*j
            
        return m
        
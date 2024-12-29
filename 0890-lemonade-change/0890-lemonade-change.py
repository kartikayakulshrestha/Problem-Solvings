class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills[0]!=5:
            return False
        
        dic={
            5:0,
            10:0,
            20:0
        }
        
        for i in range(len(bills)):
            if bills[i]==5:
                dic[5]+=1
                
            elif bills[i]==10:
                if dic[5]>=1:
                    dic[5]-=1
                    dic[10]+=1
                else:
                    return False
                
            else:
                if dic[10]>=1 and dic[5]>=1:
                    dic[5]-=1
                    dic[10]-=1
                    dic[20]+=1
                elif dic[5]>=3:
                    dic[5]-=3
                    dic[20]+=1
                else:
                    return False
            
        return True
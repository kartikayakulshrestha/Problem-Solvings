class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        n=len(intervals)
        if n==1:
            return [intervals[0]]
        ans=[]
        x=intervals[0]
        flag=1
        for i in range(1,n):
            if x[1]>=intervals[i][0]:
                x[0]=min(intervals[i][0],x[0])
                x[1]=max(intervals[i][1],x[1])
            else:
                ans.append(x)
                x=intervals[i]
                
        ans.append(x)
        return ans
        
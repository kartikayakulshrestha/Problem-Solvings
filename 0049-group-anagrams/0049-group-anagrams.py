from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedthings=[]
        for i in strs:
            sortedthings.append("".join(sorted(i)))
        dic=defaultdict(list)
        for i in range(len(strs)):
            dic[sortedthings[i]].append(strs[i])
        
        return list(dic.values())


        
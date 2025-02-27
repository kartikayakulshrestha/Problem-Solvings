class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n=len(strs)
        dic={}
        for i in range(n):
            freq = [0] * 26  

            for j in strs[i]:
                freq[ord(j) - 97] += 1  # Update frequency count

            tup = tuple(freq)  # Convert list to an immutable tuple

            if tup not in dic:
                dic[tup] = [strs[i]]
            else:
                dic[tup].append(strs[i])
        return list(dic.values())
        
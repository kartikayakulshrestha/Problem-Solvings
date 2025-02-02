
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams={}
        for word in strs:
            freq=[0]*26
            for char in word:
                freq[ord(char)-ord("a")]+=1
            p=tuple(freq)
            if p in anagrams:

                anagrams[p].append(word)
            else:
                anagrams[p]=[word]
        return list(anagrams.values())
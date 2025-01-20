class Trie:

    def __init__(self):
        self.root=[False]*26
        self.ended=False

    def insert(self, word: str) -> None:
        trie=self.root
        current=trie
        for i in range(len(word)):
            x=97-ord(word[i])
            if current[x]==False:
                current[x]=Trie()
                
            if i==len(word)-1:
                current[x].ended=True
            current=current[x].root
        
        self.root=trie
        
        return
            

    def search(self, word: str) -> bool:
        trie=self.root
        current=trie
        for i in range(len(word)):
            x=97-ord(word[i])
            
            if current[x]==False:
                return False
            
            
            if i==len(word)-1:
                if current[x].ended:
                    return True
                else:
                    return False
            current=current[x].root

    def startsWith(self,word: str) -> bool:
        trie=self.root
        current=trie
        for i in range(len(word)):
            x=97-ord(word[i])
            
            if current[x]==False:
                return False
            
            
            current=current[x].root
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
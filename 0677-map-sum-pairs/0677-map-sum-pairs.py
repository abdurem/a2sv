class TrieNode:

    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.endOfWord = False
        
class MapSum:

    def __init__(self):
        self.root = TrieNode() 
        self.d = defaultdict(int)
    def insert(self, key: str, val: int) -> None:
        self.d[key] = val
        node = self.root
        for letter in key:
            if node.children[letter] == None:
                node.children[letter] = TrieNode()
            node= node.children[letter]
        node.endOfWord = True

    def sum(self, prefix: str) -> int:
        word =""
        ans = 0
        node = self.root
        def search(node,word):
            nonlocal ans
            if node.endOfWord:
                ans += self.d[word]
            for n in node.children:
                search(node.children[n],word+n)
            return ans
            
        for letter in prefix:
            word += letter
            node = node.children[letter]
        
        ans = search(node,word)
       
            
        return ans

        

        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        root = self.root
        for w in word:
            root = root.children[w]
        root.isWord = True

    def search(self, word: str) -> bool:
        return self.helper(self.root, word)
    
    def helper(self, node, word):
        for i,w in enumerate(word):
            if w=='.':
                for child in node.children:
                    if self.helper(node.children[child],word[i+1:]):
                        return True
                return False
            else:
                if w in node.children:
                    node=node.children[w]
                else:
                    return False
                
        return node.isWord 
    

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
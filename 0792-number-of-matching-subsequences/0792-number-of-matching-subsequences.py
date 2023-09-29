class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.cache = defaultdict(bool)
    
    def addWord(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True
    
    def searchSubseq(self, word, s):
        node = self.root
        cache = self.cache
        i = 0

        if word in cache:
            return cache[word]
        

        while not node.isWord and i < len(word):
            if word[i] == list(node.children.keys())[0]:
                i+=1
            node = node.children[list(node.children.keys())[0]]  
        
        if i == len(word):
            cache[word] = True
        else:
            cache[word] = False
        
        return True if i == len(word) else False

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        trie = Trie()
        trie.addWord(s)
        ans = 0

        for w in words:
            if trie.searchSubseq(w, set()):
                ans+=1
        
        return ans
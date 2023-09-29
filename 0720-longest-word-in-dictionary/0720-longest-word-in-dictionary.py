class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isWord = False
        
class Trie:
    def __init__(self):
        self.node = TrieNode()
        
    def addWord(self, word):
        node = self.node

        for w in word:
            node = node.children[w]
        node.isWord = True
    
    def searchWord(self, word):
        node = self.node

        strs = ""
        
        for w in word:
            node = node.children[w]
            if node.isWord:
                strs += w
            else:
                strs = ""
                break
        
        return strs

class Solution:
    def longestWord(self, words: List[str]) -> str:
        tries = Trie()
        soln = ""
        
        for w in words:
            tries.addWord(w)
        
        for w in words:
            tmp = tries.searchWord(w)
            if len(tmp) > len(soln) or (len(tmp) == len(soln) and tmp < soln):
                soln = tmp

        return soln
        
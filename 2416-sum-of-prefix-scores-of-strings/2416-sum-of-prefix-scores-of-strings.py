class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isWord = False
        self.count = 0
    
class Trie:
    def __init__(self):
        self.node = TrieNode()

    def addWord(self, word):
        node = self.node

        for w in word:
            node = node.children[w] 
            node.count += 1

        node.isWord = True

    def search(self, word):
        node = self.node

        ans = 0
        for w in word:
            ans += node.children[w].count
            node = node.children[w]
        return ans

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()

        for w in words:
            trie.addWord(w)

        ans = []
        for w in words:
            ans.append(trie.search(w))
        
        return ans
        
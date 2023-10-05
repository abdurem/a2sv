class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.index = -1

class WordFilter:

    def __init__(self, words: List[str]):
        self.node = TrieNode()

        for i,word in enumerate(words):
            for j, w in enumerate(word):
                self.addWord(word[j:]+'{'+word, i)

    def f(self, pref: str, suff: str) -> int:
        word = suff+'{'+pref

        return self.search(word)
        
    def addWord(self, word, idx):
        node = self.node

        for i, w in enumerate(word):
            node = node.children[w]
            node.index = idx

    def search(self, word):
        node = self.node

        for w in word:
            node = node.children[w]
        
        return node.index


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)
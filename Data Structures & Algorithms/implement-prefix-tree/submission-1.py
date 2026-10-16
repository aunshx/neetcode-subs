class Trie:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.trie = Trie()

    def insert(self, word: str) -> None:
        currTrieNode = self.trie
        for w in word:
            if w not in currTrieNode.children:
                currTrieNode.children[w] = Trie()
            currTrieNode = currTrieNode.children[w]
        currTrieNode.endOfWord = True

    def search(self, word: str) -> bool:
        currTrieNode = self.trie
        for w in word:
            if w not in currTrieNode.children:
                return False
            currTrieNode = currTrieNode.children[w]
        return currTrieNode.endOfWord

    def startsWith(self, prefix: str) -> bool:
        currTrieNode = self.trie
        for p in prefix:
            if p not in currTrieNode.children:
                return False
            currTrieNode = currTrieNode.children[p]
        return True
        
        
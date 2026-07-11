class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.trie = TrieNode()

    def insert(self, word: str) -> None:
        currTrieNode = self.trie
        for c in word:
            if c not in currTrieNode.children:
                currTrieNode.children[c] = TrieNode()
            currTrieNode = currTrieNode.children[c]
        currTrieNode.endOfWord = True

    def search(self, word: str) -> bool:
        currTrieNode = self.trie
        for c in word:
            if c not in currTrieNode.children:
                return False
            currTrieNode = currTrieNode.children[c]
        return currTrieNode.endOfWord 
        

    def startsWith(self, prefix: str) -> bool:
        currTrieNode = self.trie
        for c in prefix:
            if c not in currTrieNode.children:
                return False
            currTrieNode = currTrieNode.children[c]
        return True 
        
        
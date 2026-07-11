class TrieNode:
    def __init__(self):
        self.children = {}
        self.isTrue = False

class Solution:
    def __init__(self):
        self.trie = TrieNode()
        self.visited = set()
        self.ROWS = 0
        self.COLS = 0

    def dfs(self, r, c, node, word, res):
        if (r < 0 or r >= self.ROWS or c < 0 or c >= self.COLS or (r,c) in self.visited or self.board[r][c] not in node.children):
            return
        self.visited.add((r,c))
        node = node.children[self.board[r][c]]
        word += self.board[r][c]

        if node.isTrue:
            res.add(word)

        self.dfs(r+1, c, node, word, res)
        self.dfs(r-1, c, node, word, res)
        self.dfs(r, c+1, node, word, res)
        self.dfs(r, c-1, node, word, res)

        self.visited.remove((r,c))


    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.ROWS = len(board)
        self.COLS = len(board[0])
        res = set()
        self.board = board

        for word in words:
            curr = self.trie
            for w in word:
                if w not in curr.children:
                    curr.children[w] = TrieNode()
                curr = curr.children[w]
            curr.isTrue = True 

        for r in range(self.ROWS):
            for c in range(self.COLS):
                self.dfs(r, c, self.trie, '', res)

        return list(res)


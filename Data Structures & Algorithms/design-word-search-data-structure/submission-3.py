class TrieNode:
    def __init__(self):
        # Mảng 26 phần tử tương ứng a-z
        self.children = [None] * 26
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.is_end = True

    def search(self, word: str) -> bool:
        def dfs(idx, node):
            curr = node
            for i in range(idx, len(word)):
                char = word[i]
                if char == '.':
                    # Duyệt qua tất cả 26 nhánh con có thể có
                    for child in curr.children:
                        if child and dfs(i + 1, child):
                            return True
                    return False
                else:
                    child_idx = ord(char) - ord('a')
                    if not curr.children[child_idx]:
                        return False
                    curr = curr.children[child_idx]
            return curr.is_end

        return dfs(0, self.root)
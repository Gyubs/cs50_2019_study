class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        tree = self.trie
        for char in word:
            if char not in tree:
                tree[char] = {}
            tree = tree[char]
        tree['*'] = True

    def search(self, word: str) -> bool:
        tree = self.trie
        for char in word:
            if char not in tree:
                return False
            print(char)
            print(tree)
            tree = tree[char]
        return '*' in tree

    def startsWith(self, prefix: str) -> bool:
        tree = self.trie
        for char in prefix:
            if char not in tree:
                return False
            tree = tree[char]
            print(tree)
        return True

word = "apple"
prefix = "app"
obj = Trie()
obj.insert(word)
param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
print("search: " + str(param_2))
# print("startsWith: " + str(param_3))
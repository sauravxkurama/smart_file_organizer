class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.full_word = ""

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word.lower():  # case insensitive
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True
        node.full_word = word

    def search_prefix(self, prefix):
        node = self.root
        for ch in prefix.lower():
            if ch not in node.children:
                return []
            node = node.children[ch]
        return self._collect_all_words(node)

    def _collect_all_words(self, node):
        results = []
        if node.is_end:
            results.append(node.full_word)
        for child in node.children.values():
            results.extend(self._collect_all_words(child))
        return results

import unittest
from prefix_tree import Trie


class TestTrie(unittest.TestCase):

    def test_example_from_problem(self):
        """Тест примера c leetcode :)"""
        trie = Trie()
        trie.insert("apple")
        self.assertTrue(trie.search("apple"))
        self.assertFalse(trie.search("app"))
        self.assertTrue(trie.startsWith("app"))
        trie.insert("app")
        self.assertTrue(trie.search("app"))

    def test_insert_and_search_single_word(self):
        """Вставка и поиск одного слова"""
        trie = Trie()
        trie.insert("hello")
        self.assertTrue(trie.search("hello"))
        self.assertFalse(trie.search("hell"))
        self.assertFalse(trie.search("world"))

    def test_starts_with_prefix(self):
        """Проверка префиксов"""
        trie = Trie()
        trie.insert("apple")
        self.assertTrue(trie.startsWith("app"))
        self.assertFalse(trie.startsWith("apx"))
        self.assertTrue(trie.startsWith("apple"))

    def test_empty_trie(self):
        """Пустое дерево"""
        trie = Trie()
        self.assertFalse(trie.search(""))
        self.assertFalse(trie.search("any"))
        self.assertFalse(trie.startsWith("a"))

    def test_overlapping_words(self):
        """Слова с общими префиксами"""
        trie = Trie()
        trie.insert("app")
        trie.insert("apple")

        self.assertTrue(trie.search("app"))
        self.assertTrue(trie.search("apple"))
        self.assertTrue(trie.startsWith("appl"))

        self.assertFalse(trie.search("apl"))

    def test_multiple_inserts(self):
        """Множественные вставки"""
        trie = Trie()
        words = ["cat", "car", "cart", "cater"]
        for word in words:
            trie.insert(word)

        self.assertTrue(trie.search("cat"))
        self.assertTrue(trie.search("car"))
        self.assertTrue(trie.search("cart"))
        self.assertTrue(trie.search("cater"))

        self.assertFalse(trie.search("ca"))
        self.assertTrue(trie.startsWith("ca"))

    def test_partial_word_not_considered(self):
        """Части слова не считаются полными"""
        trie = Trie()
        trie.insert("test")
        self.assertFalse(trie.search("tes"))
        self.assertTrue(trie.startsWith("tes"))

    def test_insert_empty_string(self):
        """Вставка пустой строки (если разрешено)"""
        trie = Trie()
        trie.insert("")
        self.assertTrue(trie.search(""))
        self.assertTrue(trie.startsWith(""))


if __name__ == "__main__":
    unittest.main()

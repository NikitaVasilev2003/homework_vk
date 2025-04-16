# design_add_and_search_words.py
import unittest
from design_add_and_search_words import WordDictionary


class TestWordDictionary(unittest.TestCase):

    def test_example_from_problem(self):
        """Тест примера с leetcode :)"""
        wd = WordDictionary()
        wd.addWord("bad")
        wd.addWord("dad")
        wd.addWord("mad")

        self.assertFalse(wd.search("pad"))  # False
        self.assertTrue(wd.search("bad"))  # True
        self.assertTrue(wd.search(".ad"))  # True
        self.assertTrue(wd.search("b.."))  # True

    def test_exact_match(self):
        """Поиск точного совпадения"""
        wd = WordDictionary()
        wd.addWord("apple")
        self.assertTrue(wd.search("apple"))
        self.assertFalse(wd.search("app"))

    def test_wildcard_queries(self):
        """Поиск с подстановочными символами"""
        wd = WordDictionary()
        wd.addWord("cat")
        wd.addWord("car")
        wd.addWord("camp")

        # Проверка различных комбинаций
        self.assertTrue(wd.search("c.t"))  # "cat"
        self.assertTrue(wd.search(".a."))  # "cat", "car"
        self.assertTrue(wd.search("ca.."))  # "camp"
        self.assertTrue(wd.search("c..p"))  # Не существует

    def test_multiple_wildcards(self):
        """Несколько подстановочных символов в запросе"""
        wd = WordDictionary()
        wd.addWord("test")
        wd.addWord("text")
        wd.addWord("temp")

        self.assertTrue(wd.search("t..t"))
        self.assertTrue(wd.search(".e.t"))
        self.assertTrue(wd.search("t..p"))

    def test_empty_word(self):
        """Работа с пустой строкой (если разрешено)"""
        wd = WordDictionary()
        wd.addWord("")
        self.assertTrue(wd.search(""))
        self.assertFalse(wd.search("a"))

    def test_words_of_different_lengths(self):
        """Слова разной длины"""
        wd = WordDictionary()
        wd.addWord("a")
        wd.addWord("ab")
        wd.addWord("abc")

        self.assertTrue(wd.search("a"))
        self.assertTrue(wd.search(".b"))
        self.assertTrue(wd.search("a.c"))
        self.assertFalse(wd.search("abcd"))

    def test_overlapping_words(self):
        """Перекрывающиеся слова"""
        wd = WordDictionary()
        wd.addWord("bad")
        wd.addWord("bed")
        wd.addWord("bid")

        self.assertTrue(wd.search("b.d"))
        self.assertTrue(wd.search("b.."))
        self.assertFalse(wd.search("b..d"))

    def test_deep_recursion(self):
        """Глубокий поиск с подстановками"""
        wd = WordDictionary()
        wd.addWord("abcdefghijk")
        self.assertTrue(wd.search("a.c.e.g...k"))
        self.assertFalse(wd.search("a.c.e.g..z"))


if __name__ == "__main__":
    unittest.main()

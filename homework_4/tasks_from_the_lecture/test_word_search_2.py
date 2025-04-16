import unittest
from word_search_2 import findWords


class TestWordSearch2(unittest.TestCase):

    def test_example_1(self):
        board = [
            ["o", "a", "a", "n"],
            ["e", "t", "a", "e"],
            ["i", "h", "k", "r"],
            ["i", "f", "l", "v"],
        ]
        words = ["oath", "pea", "eat", "rain"]
        result = findWords(board, words)
        self.assertCountEqual(result, ["eat", "oath"])

    def test_example_2(self):
        board = [["a", "b"], ["c", "d"]]
        words = ["abcb"]
        self.assertEqual(findWords(board, words), [])

    def test_empty_board(self):
        self.assertEqual(findWords([[]], ["test"]), [])

    def test_empty_words(self):
        board = [["a"]]
        self.assertEqual(findWords(board, []), [])

    def test_single_cell_matching_word(self):
        board = [["a"]]
        words = ["a"]
        self.assertEqual(findWords(board, words), ["a"])

    def test_word_with_reused_letter(self):
        board = [["a", "b"], ["c", "a"]]
        words = ["abaca"]
        self.assertEqual(findWords(board, words), [])

    def test_multiple_paths(self):
        board = [["a", "b"], ["c", "d"]]
        words = ["acdb", "abdc", "cdba"]
        self.assertIn("acdb", findWords(board, words))

    def test_overlapping_words(self):
        board = [["o", "a"], ["e", "t"]]
        words = ["oat", "eat", "oe"]
        result = findWords(board, words)
        expected = ["oat", "oe"]
        self.assertCountEqual(result, expected)

    def test_long_word_exceeding_board_size(self):
        board = [["a", "b"], ["c", "d"]]
        words = ["abcdc"]
        self.assertEqual(findWords(board, words), [])

    def test_words_with_same_prefix(self):
        board = [["a", "p"], ["p", "l"]]
        words = ["ap", "app", "apple"]
        result = findWords(board, words)
        self.assertCountEqual(result, ["ap"])  # Только "ap" возможно


if __name__ == "__main__":
    unittest.main()

import unittest
from t_3_2 import feedAnimals

# я не писал два файла для тестов, но назвал фунции одинаково, поэтому для текстирования
# другого случая достаточно написать
# from t_3_1 import feedAnimals


class TestFeedAnimals(unittest.TestCase):
    def test_first(self):
        """1 пример с семинара"""
        result = feedAnimals([3, 4, 7], [8, 1, 2])
        self.assertEqual(1, result)

    def test_second(self):
        """2 пример с семинара"""
        result = feedAnimals([3, 8, 1, 4], [1, 1, 2])
        self.assertEqual(1, result)

    def test_third(self):
        """3 пример с семинара"""
        result = feedAnimals([8, 2, 3, 2], [1, 4, 3, 8])
        self.assertEqual(3, result)

    def test_zero_food(self):
        """Пустой список еды"""
        result = feedAnimals([], [1, 4, 3, 8])
        self.assertEqual(0, result)

    def test_zero_animals(self):
        """Пустой список животных"""
        result = feedAnimals([1, 4, 3, 8], [])
        self.assertEqual(0, result)


if __name__ == "__main__":
    unittest.main()

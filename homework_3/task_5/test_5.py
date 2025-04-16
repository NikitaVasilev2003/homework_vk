import unittest
from t_5_2 import twoSum

# я не писал два файла для тестов, но назвал фунции одинаково, поэтому для текстирования
# другого случая достаточно написать
# from t_5_1 import twoSum


class TestTwoSum(unittest.TestCase):
    def test_base_case(self):
        """Базовый пример, когда есть в массиве нужные элементы"""
        result = twoSum([2, 7, 11, 15], 9)
        self.assertEqual((0, 1), result)

    def test_negative_case(self):
        """В массиве нет элементов, дающих необходимый"""
        result = twoSum([3, 2, 4], 6)
        self.assertEqual([], result)

    def test_two_identical_elements(self):
        """2 одинаковых элемента"""
        result = twoSum([3, 3], 6)
        self.assertEqual((0, 1), result)

    def test_zero_array(self):
        """Пустой список еды"""
        result = twoSum([], 4)
        self.assertEqual([], result)


if __name__ == "__main__":
    unittest.main()

import unittest
from main_8 import *


class MyTestCase(unittest.TestCase):

    def test_read_file(self):
        path = "./demo.c"
        # print(read_file(path))

    def test_count_keywords(self):
        text = read_file("./demo.c")
        self.assertEqual(count_keywords(text), 35)

    def test_count_if_else(self):
        text = read_file("./demo.c")
        result = count_if_else_etc(text)
        self.assertEqual(result, [2, 2])


if __name__ == '__main__':
    unittest.main()

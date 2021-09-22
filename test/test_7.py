import unittest
from main_7 import *


class MyTestCase(unittest.TestCase):
    def setUp(self):
        print("Start")

    def test_read_file(self):
        path = "./demo.c"
        # print(read_file(path))

    def test_count_keywords(self):
        text = read_file("./demo.c")
        self.assertEqual(count_keywords(text), 35)

    def test_count_if_else(self):
        text = read_file("./demo.c")
        self.assertEqual(count_if_else(text), 2)

    def test_count_if_elseif_else(self):
        text = read_file("./demo.c")
        text = remove_if_else(text)
        self.assertEqual(count_if_elseif_else(text), 2)

    def tearDown(self):
        print("End")


if __name__ == '__main__':
    unittest.main()

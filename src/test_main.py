import unittest
import main

# Unit Test
class TestMain(unittest.TestCase):
    def test_hello(self):
        # hello() が 'hello'と返しているならOK
        self.assertEqual(main.hello(), 'hello')

if __name__ == '__main__':
    unittest.main()



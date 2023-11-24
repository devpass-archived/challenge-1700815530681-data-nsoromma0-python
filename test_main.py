import unittest
from main import Stack

class TestMain(unittest.TestCase):
    def test_stack(self):
        stack = Stack()
        stack.push('A')
        stack.push('B')
        stack.push('C')

        self.assertEqual(stack.pop(), 'C')
        self.assertEqual(stack.peek(), 'B')

if __name__ == '__main__':
    unittest.main()

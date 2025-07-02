def square(num):
    return num * 2   # Here we have a bug. to check for unit testing.

import unittest
class Square_Test(unittest.TestCase):


    def test_square_num(self):
        result_1 = square(5)  # Expected is -> 25  # also check with 2 also
        self.assertEqual(result_1,25)

    def test_string_input(self):
        result_2 = square("a") # Expected is -> invalid input
        self.assertEqual(result_2,"Invalid input")
    

if __name__ == "__main__":
    unittest.main()

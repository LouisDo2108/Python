import unittest
import cap

class test(unittest.TestCase):

    def test_one(self):
        text =  "python"
        result = cap.Cap(text)
        self.assertEqual(result, "Python") 
    
    def test_two(self):
        text =  "python"
        result = cap.Count(text)
        self.assertEqual(result, 2) 

if __name__ == "__main__":
    unittest.main()
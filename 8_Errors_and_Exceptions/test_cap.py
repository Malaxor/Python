'''
unittest of cap.cap_text() capitalization of one word string and multiple words string
'''
import unittest
import cap

class TestCap(unittest.TestCase):
   '''
   this class inherits methods from unittest.TestCase for testing a local module
   '''
   def test_one_word(self):
      """
      one word string capitalization testing
      """
      text = 'python'
      result = cap.cap_text(text)
      self.assertEqual(result, 'Python')

   def test_multiple_words(self):
      '''
      multiple word string capitalization testing
      '''
      text = 'monty python'
      result = cap.cap_text(text)
      self.assertEqual(result, 'Monty Python')

if __name__ == '__main__':
   unittest.main()

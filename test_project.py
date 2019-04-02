import unittest
from FileProducer import Book

class test_Book(unittest.TestCase):

    def test1(self):
        test_string1 = "this is a a test"
        book1 = Book('test_name1',test_string1)
        book1_dict = book1.countWords()
        test_dict1 = {'this':1,'is':1,'a':2,'test':1}
        self.assertDictEqual(test_dict1,book1_dict)
       
    
    def test2(self):
        test_string2 = "this is also a test!!"
        book2 = Book('test_name2',test_string2)
        book2_dict = book2.countWords()
        test_dict2 = {'this':1,'is':1, 'also':1, 'a':1,'test!!':1}
        self.assertDictEqual(test_dict2,book2_dict)

if __name__ == '__main__':
    unittest.main()
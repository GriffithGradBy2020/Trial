import unittest
import test


class TestFinal(unittest.TestCase):

    def test_same(self):
        self.assertEqual(test.same('lead', 'lead'), 4)
        self.assertEqual(test.same('lead', 'gold'), 1)
        self.assertEqual(test.same('hide', 'seek'), 0)
        self.assertNotEqual(test.same('hide', 'lead'), 3)




    def test_fileInput(self):
        self.assertTrue(test.fileInput("dictionary.txt"), True)
        self.assertTrue(test.fileInput("NotRealDictionary.txt"), False)



    def test_startInput(self):
        self.assertTrue(test.startInput("lead"), True)
        self.assertFalse(test.startInput("123"), False)
        self.assertFalse(test.startInput(" "), False)

    def test_targetInput(self):
        self.assertTrue(test.startInput("gold"), True)
        self.assertFalse(test.startInput("123"), False)
        self.assertFalse(test.startInput(" "), False)

    def test_find(self):

        self.assertEqual(test.find('lead', test.words, test.seen, 'gold', test.path), False)
        #self.assertEqual(test.find('hide', test.words, test.seen, 'seek', test.path), False)
        #self.assertEqual(test.find('lead', test.words, test.seen, 'lead', test.path), True)

    #def test_build(self):

    def test_matchingInput(self):
        self.assertTrue(test.matchingInput("lead","gold"))
        self.assertFalse(test.matchingInput("lead", "golds"))




if __name__ == '__main__':
    unittest.main()
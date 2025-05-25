import unittest

import Notes

testNoteSeries = ['a', 'cs', 'e']
testRhythmSeries = ['2', '4', '8']
testRange = ()

class TestMeasure(unittest.TestCase):
    
    def test_getNote(self):
        note = Notes.getNote(0, 0, testNoteSeries, 0, testRhythmSeries)
        
        self.assertEqual("a'2 ", note)
        
        note = Notes.getNote(0, 4, testNoteSeries, 0, testRhythmSeries)
        
        self.assertEqual("a''''2 ", note)
        
        note = Notes.getNote(0, -1, testNoteSeries, 0, testRhythmSeries)
        
        self.assertEqual("a,2 ", note)
    
    def test_getRandomNoteValid(self):
        note = Notes.getRandomNote(series = ['a'])
        
        self.assertIn('a', note)
        
        note = Notes.getRandomNote(range = (4, 5))
        
        self.assertIn("''''", note)
        
        note = Notes.getRandomNote(rhythms = ["4"])
        
        self.assertIn('4', note)
        
    def test_getRandomNoteInvalid(self):
        note = Notes.getRandomNote(series = [])
        
        self.assertIsNone(note)
        
        note = Notes.getRandomNote(range = (4))
        
        self.assertIsNone(note)
        
        note = Notes.getRandomNote(range = (4, 5, 6))
        
        self.assertIsNone(note)
        
        note = Notes.getRandomNote(rhythms = [])
        
        self.assertIsNone(note)
    
if __name__ == '__main__':
    unittest.main()
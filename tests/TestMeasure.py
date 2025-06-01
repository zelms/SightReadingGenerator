import unittest

from src.Measure import Measure
import src.Notes as Notes

class TestMeasure(unittest.TestCase):

    #Get measure string
    def test_getMeasureStr(self):
        testMeasure = Measure(4, 4)

        note = Notes.getRandomNote()

        testMeasure.addNote(note)

        self.assertEqual(note, testMeasure.getMeasureStr())

    #Clearing measure of notes
    def test_clearMeasure(self):
        testMeasure = Measure(4, 4)

        testMeasure.addNote(Notes.getRandomNote())

        filled = len(testMeasure.getMeasureStr()) > 0

        self.assertTrue(filled) #Measure has something

        testMeasure.clearMeasure()

        filled = len(testMeasure.getMeasureStr()) == 0

        self.assertTrue(filled) #Measure is cleared

        

    #Fill with quarter notes, making sure each one gets added
    def test_addNote(self):
        testMeasure = Measure(4, 4)

        spaceLeft = testMeasure.addNote("c'4")

        self.assertEqual("c'4", testMeasure.getMeasureStr())

        self.assertAlmostEqual(3.0, spaceLeft)  #Accurate up to 7 decimal places

        spaceLeft = testMeasure.addNote("d'4")

        self.assertEqual("c'4d'4", testMeasure.getMeasureStr())

        self.assertAlmostEqual(2.0, spaceLeft)

        spaceLeft = testMeasure.addNote("e'4")

        self.assertEqual("c'4d'4e'4", testMeasure.getMeasureStr())

        self.assertAlmostEqual(1.0, spaceLeft)

        spaceLeft = testMeasure.addNote("f'4")
        
        self.assertEqual("c'4d'4e'4f'4", testMeasure.getMeasureStr())

        self.assertAlmostEqual(0.0, spaceLeft)
        
    #Attempt to overfill with different sized notes
    def test_addNoteOverfill(self):
        #Filling all the way with just quarter notes
        testMeasure = Measure(4, 4)
        spaceLeft = testMeasure.addNote("c'4")
        spaceLeft = testMeasure.addNote("d'4")
        spaceLeft = testMeasure.addNote("e'4")
        spaceLeft = testMeasure.addNote("f'4")
        
        #Trying to add one more quarter note
        spaceLeft = testMeasure.addNote("g'4")
        
        self.assertEqual("c'4d'4e'4f'4", testMeasure.getMeasureStr())

        self.assertAlmostEqual(0.0, spaceLeft)
        
        #Try overfill with larger notes
        #Whole notes and half notes
        testMeasure.clearMeasure()

        addedNote = Notes.getNote(0, 1, Notes.mixedSeries, 1, Notes.commonRhythms)

        testMeasure.addNote(addedNote)

        addedNote = Notes.getNote(1, 1, Notes.mixedSeries, 0, Notes.commonRhythms)

        spaceLeft = testMeasure.addNote(addedNote)

        self.assertAlmostEqual(0.0, spaceLeft)

        #Half notes and quarter notes
        testMeasure.clearMeasure()

        addedNote = Notes.getNote(0, 1, Notes.mixedSeries, 1, Notes.commonRhythms)

        testMeasure.addNote(addedNote)

        addedNote = Notes.getNote(1, 1, Notes.mixedSeries, 2, Notes.commonRhythms)
        
        testMeasure.addNote(addedNote)
        
        addedNote = Notes.getNote(0, 1, Notes.mixedSeries, 1, Notes.commonRhythms)

        spaceLeft = testMeasure.addNote(addedNote)

        self.assertAlmostEqual(0.0, spaceLeft)
        
        # Quarter and eighth notes
        testMeasure.clearMeasure()

        addedNote = Notes.getNote(0, 1, Notes.mixedSeries, 2, Notes.commonRhythms)

        testMeasure.addNote(addedNote)
        testMeasure.addNote(addedNote)
        testMeasure.addNote(addedNote)

        addedNote = Notes.getNote(1, 1, Notes.mixedSeries, 3, Notes.commonRhythms)
        
        testMeasure.addNote(addedNote)
        
        addedNote = Notes.getNote(0, 1, Notes.mixedSeries, 2, Notes.commonRhythms)

        spaceLeft = testMeasure.addNote(addedNote)

        self.assertAlmostEqual(0.0, spaceLeft)


if __name__ == '__main__':
    unittest.main()
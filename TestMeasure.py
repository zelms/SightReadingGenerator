from Measure import Measure
import Notes

def test_getMeasureStr():
    testMeasure = Measure(4, 4)

    print("=== Adding one note ===")

    note = Notes.getRandomNote()

    testMeasure.addNote(note)

    print("Expected:", note)
    print("Actual: ", testMeasure.getMeasureStr())

def test_clearMeasure():
    testMeasure = Measure(4, 4)

    print("=== Filling measure ===")

    testMeasure.addNote(Notes.getRandomNote())

    filled = len(testMeasure.getMeasureStr()) > 0

    print("Expected: True")
    print("Actual: ", filled)

    print("=== Clearing measure ===")

    testMeasure.clearMeasure()

    filled = len(testMeasure.getMeasureStr()) == 0

    print("Expected: True")
    print("Actual: ", filled)

    

def test_addNote():
    testMeasure = Measure(4, 4)

    print("=== Adding One Quarter Note ===")

    spaceLeft = testMeasure.addNote("c'4")

    print("Expected: c'4")
    print("Actual:  ", testMeasure.getMeasureStr())

    print("Expected: 3.0")
    print("Actual: ", spaceLeft)

    print("=== Filling the measure ===")

    print("- Adding second note")
    spaceLeft = testMeasure.addNote("d'4")

    print("Expected: c'4d'4")
    print("Actual:  ", testMeasure.getMeasureStr())

    print("Expected: 2.0")
    print("Actual: ", spaceLeft)

    print("- Adding third note")
    spaceLeft = testMeasure.addNote("e'4")

    print("Expected: c'4d'4e'4")
    print("Actual:  ", testMeasure.getMeasureStr())

    print("Expected: 1.0")
    print("Actual: ", spaceLeft)

    print("- Adding fourth note")
    spaceLeft = testMeasure.addNote("f'4")
    
    print("Expected: c'4d'4e'4f'4")
    print("Actual:  ", testMeasure.getMeasureStr())

    print("Expected: 0.0")
    print("Actual: ", spaceLeft)

    print("=== Attempting to overfill ===")

    spaceLeft = testMeasure.addNote("g'4")
    
    print("Expected: c'4d'4e'4f'4")
    print("Actual:  ", testMeasure.getMeasureStr())

    print("Expected: 0.0")
    print("Actual: ", spaceLeft)

    print("=== Refilling with notes too big ===")
    
    print("- Whole and half notes")

    testMeasure.clearMeasure()

    addedNote = Notes.getNote(0, 1, Notes.mixedSeries, 1, Notes.noteDurations)

    testMeasure.addNote(addedNote)

    addedNote = Notes.getNote(1, 1, Notes.mixedSeries, 0, Notes.noteDurations)

    spaceLeft = testMeasure.addNote(addedNote)

    print("Expected: -2.0")
    print("Actual: ", spaceLeft)
    
    print("- Half and quarter notes")
    
    testMeasure.clearMeasure()

    addedNote = Notes.getNote(0, 1, Notes.mixedSeries, 1, Notes.noteDurations)

    testMeasure.addNote(addedNote)

    addedNote = Notes.getNote(1, 1, Notes.mixedSeries, 2, Notes.noteDurations)
    
    testMeasure.addNote(addedNote)
    
    addedNote = Notes.getNote(0, 1, Notes.mixedSeries, 1, Notes.noteDurations)

    spaceLeft = testMeasure.addNote(addedNote)

    print("Expected: -1.0")
    print("Actual: ", spaceLeft)
    
    print("- Quarter and eighth notes")
    
    testMeasure.clearMeasure()

    addedNote = Notes.getNote(0, 1, Notes.mixedSeries, 2, Notes.noteDurations)

    testMeasure.addNote(addedNote)
    testMeasure.addNote(addedNote)
    testMeasure.addNote(addedNote)

    addedNote = Notes.getNote(1, 1, Notes.mixedSeries, 3, Notes.noteDurations)
    
    testMeasure.addNote(addedNote)
    
    addedNote = Notes.getNote(0, 1, Notes.mixedSeries, 2, Notes.noteDurations)

    spaceLeft = testMeasure.addNote(addedNote)

    print("Expected: -0.5")
    print("Actual: ", spaceLeft)

def runTests():
    test_getMeasureStr()
    test_clearMeasure()
    test_addNote()


if __name__ == "__main__":
    runTests()
import abjad
from SightReadingGenerator import Notes, Measure

cMajorSeries = ['c', 'd', 'e', 'f', 'g', 'a', 'b']
fMinorSeries = ['f', 'g', 'af', 'bf', 'c', 'df', 'ef']
wholeToneSeries = ['c', 'd', 'e', 'fs', 'gs', 'as']
rhythmSeries = ['1', '2', '4', '8']

def main():
    numNotes = 24
    measures = numNotes // 4
    
    measureList = []
    for i in range(measures):
        measureList.append(Measure.Measure(4, 4))

    idx = 0
    for j in range(measures):
        spaceLeft = measureList[idx].addNote(Notes.getRandomNote(wholeToneSeries, rhythms=rhythmSeries))
        while(spaceLeft > 0):
            spaceLeft = measureList[idx].addNote(Notes.getRandomNote(wholeToneSeries, rhythms=rhythmSeries))
        idx = idx + 1

    string = ""
    for k in range(measures):
        string = string + measureList[k].getMeasureStr()

    voice_1 = abjad.Voice(string, name="Voice_1")
    staff_1 = abjad.Staff([voice_1], name="Staff_1")
    abjad.show(staff_1)


if __name__ == "__main__":
    main()
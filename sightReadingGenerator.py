# Sight Reading Generator

import abjad
import random
import re

sharpSeries = ['c', 'cs', 'd', 'ds', 'e', 'f', 'fs', 'g', 'gs', 'a', 'as', 'b']
flatSeries = ['c', 'df', 'd', 'ef', 'e', 'f', 'gf', 'g', 'af', 'a', 'bf', 'b']
mixedSeries = ['c', 'cs', 'd', 'ef', 'e', 'f', 'fs', 'g', 'af', 'a', 'bf', 'b']
noteDurations = ['1', '2', '4', '8', '16']

class Measure:
    def __init__(self, numBeats, beatDuration):
        self.maxBeats = numBeats
        self.beatDuration = beatDuration
        self.currentBeatCount = 0.0
        self.notes = ""
        
    def addNote(self, note):
        duration = int(re.findall(r'\d+', note)[0])
        
        if(duration <= 0 or duration > 32):
            print("addNote(): Invalid note input")
            
        beatLength = self.beatDuration / duration
        
        if(self.currentBeatCount == self.maxBeats):
            return 0.0
        elif(self.currentBeatCount + beatLength <= self.maxBeats):
            self.currentBeatCount = self.currentBeatCount + beatLength
            self.notes = self.notes + note 
            return self.maxBeats - self.currentBeatCount
        else:
            desiredLength = self.maxBeats - self.currentBeatCount # Still a float
            newDuration = self.beatDuration / desiredLength
            note = note.replace(str(int(duration)), str(int(newDuration)))
            self.currentBeatCount = self.currentBeatCount + desiredLength
            self.notes = self.notes + note 
            return desiredLength - beatLength
        
        
        
    def getMeasureStr(self):
        return self.notes
        
def getNote(noteIdx, octave, notes, rhythmIdx, rhythm):
    if(octave > 0):
        return notes[noteIdx] + ("'" * octave) + rhythm[rhythmIdx] + " "
    if (octave == 0):
        return notes[noteIdx] + "'" + rhythm[rhythmIdx] + " "
    return notes[noteIdx] + ("," * abs(octave)) + rhythm[rhythmIdx] + " "

def getRandomNote():
    return getNote(random.randrange(0, len(mixedSeries)), random.randrange(0, 3), mixedSeries, random.randrange(0, 3), noteDurations)


def main():
    numNotes = 24
    measures = 24 // 4
    
    measureList = []
    for i in range(measures):
        measureList.append(Measure(4, 4))

    idx = 0
    for j in range(measures):
        spaceLeft = measureList[idx].addNote(getRandomNote())
        while(spaceLeft > 0):
            spaceLeft = measureList[idx].addNote(getRandomNote())
        idx = idx + 1

    string = ""
    for k in range(measures):
        string = string + measureList[k].getMeasureStr()

    # print(string)

    voice_1 = abjad.Voice(string, name="Voice_1")
    staff_1 = abjad.Staff([voice_1], name="Staff_1")
    abjad.show(staff_1)


if __name__ == "__main__":
    main()
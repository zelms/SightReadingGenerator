import random

sharpSeries = ['c', 'cs', 'd', 'ds', 'e', 'f', 'fs', 'g', 'gs', 'a', 'as', 'b']
flatSeries = ['c', 'df', 'd', 'ef', 'e', 'f', 'gf', 'g', 'af', 'a', 'bf', 'b']
mixedSeries = ['c', 'cs', 'd', 'ef', 'e', 'f', 'fs', 'g', 'af', 'a', 'bf', 'b']
noteDurations = ['1', '2', '4', '8', '16', '32']

def getNote(noteIdx, octave, notes, rhythmIdx, rhythm):
    if(octave > 0):
        return notes[noteIdx] + ("'" * octave) + rhythm[rhythmIdx] + " "
    if (octave == 0):
        return notes[noteIdx] + "'" + rhythm[rhythmIdx] + " "
    return notes[noteIdx] + ("," * abs(octave)) + rhythm[rhythmIdx] + " "

def getRandomNote(series = mixedSeries):
    return getNote(random.randrange(0, len(series)), random.randrange(0, 3), series, random.randrange(0, len(noteDurations)-2), noteDurations)
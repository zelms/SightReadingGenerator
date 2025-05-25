import random

sharpSeries = ['c', 'cs', 'd', 'ds', 'e', 'f', 'fs', 'g', 'gs', 'a', 'as', 'b']
flatSeries = ['c', 'df', 'd', 'ef', 'e', 'f', 'gf', 'g', 'af', 'a', 'bf', 'b']
mixedSeries = ['c', 'cs', 'd', 'ef', 'e', 'f', 'fs', 'g', 'af', 'a', 'bf', 'b']
commonRhythms = ['1', '2', '4', '8', '16']
trebleMiddleRange = (0, 3)

def getNote(noteIdx, octave, notes, rhythmIdx, rhythm):
    if(octave > 0):
        return notes[noteIdx] + ("'" * octave) + rhythm[rhythmIdx] + " "
    if (octave == 0):
        return notes[noteIdx] + "'" + rhythm[rhythmIdx] + " "
    return notes[noteIdx] + ("," * abs(octave)) + rhythm[rhythmIdx] + " "

def getRandomNote(series = mixedSeries, range = trebleMiddleRange, rhythms = commonRhythms):
    if(len(series) == 0):
        print("Invalid note series! Make sure the series has at least one note")
        return ""
    
    if(len(range) != 2):
        print("Invalid range! Make sure range is a tuple containing two elements")
        return ""
        
    if(len(rhythms) == 0):
        print("Invalid rhythm series! Make sure the series has at least one rhythm")
        return ""    
        
    return getNote(random.randrange(0, len(series)), random.randrange(range[0], range[1]), series, random.randrange(1, len(rhythms)), rhythms)
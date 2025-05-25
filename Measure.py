import re
        
class Measure:
    def __init__(self, numBeats, beatDuration):
        self.mMaxBeats = numBeats
        self.nBeatDuration = beatDuration
        self.mCurrentBeatCount = 0.0
        self.notes = ""
        
    def addNote(self, note):
        nDuration = int(re.findall(r'\d+', note)[0])
        
        if(nDuration <= 0 or nDuration > 32):
            print("addNote(): Invalid note input")
            
        nBeatLength = self.nBeatDuration / nDuration
        
        if(self.mCurrentBeatCount == self.mMaxBeats):
            return 0.0
        elif(self.mCurrentBeatCount + nBeatLength <= self.mMaxBeats):
            self.mCurrentBeatCount = self.mCurrentBeatCount + nBeatLength
            self.notes = self.notes + note 
            return self.mMaxBeats - self.mCurrentBeatCount
        else:
            nFillMeasureLength = self.mMaxBeats - self.mCurrentBeatCount
            nNewDuration = self.nBeatDuration / nFillMeasureLength
            
            if(not nNewDuration.is_integer() or int(nNewDuration).bit_count() != 1): # If not a power of 2
                bits = int(nNewDuration).bit_length()
                nNewDuration = 1 << bits    #Round up to a power of two
                
            nNewLength = self.nBeatDuration / nNewDuration
            
            note = note.replace(str(int(nDuration)), str(int(nNewDuration)))
            self.mCurrentBeatCount = self.mCurrentBeatCount + nNewLength
            self.notes = self.notes + note 
            return self.mMaxBeats - self.mCurrentBeatCount
        
    def getMeasureStr(self):
        return self.notes
    
    def clearMeasure(self):
        self.notes = ""
        self.mCurrentBeatCount = 0.0
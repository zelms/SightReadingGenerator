import re
        
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
            desiredLength = self.maxBeats - self.currentBeatCount
            newDuration = self.beatDuration / desiredLength
            
            if(not newDuration.is_integer() or int(newDuration).bit_count() != 1): # If not a power of 2
                bits = int(newDuration).bit_length()
                newDuration = 1 << bits
                
            newLength = self.beatDuration / newDuration
            
            note = note.replace(str(int(duration)), str(int(newDuration)))
            self.currentBeatCount = self.currentBeatCount + newLength
            self.notes = self.notes + note 
            return self.maxBeats - self.currentBeatCount
        
    def getMeasureStr(self):
        return self.notes
    
    def clearMeasure(self):
        self.notes = ""
        self.currentBeatCount = 0.0
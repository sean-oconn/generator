import random
class Generator:
    """Generates random text based on k-grams of an existing sample."""

    def __init__(self, source, k):
        """Construct a new generate using the source string and model of k-grams."""
        # do all necessary preprocessing at the time of construction
        #declaring variables and splitting source into a list
        self._k=2
        v=self._k
        self._nextCharCount=0
        self._source='aaabaaacaaadaaabaaabaaac'
        sourceSplit=list(self._source)
        self._prePros={}
        q=0
        lastLet=''.join(sourceSplit[len(self._source)-2:len(self._source)])
        #for loop that will put all probability into a dictionary
        for x in range(len(sourceSplit)):
            if v<len(self._source):
                sourceJoin=''.join(sourceSplit[x:v])
                nextLet=sourceSplit[v]

                if sourceJoin not in self._prePros:
                    self._prePros[sourceJoin]={}
                if nextLet not in self._prePros[sourceJoin]:
                    self._prePros[sourceJoin][nextLet]=q
                if nextLet in self._prePros[sourceJoin]:
                    self._prePros[sourceJoin][nextLet]+=1
                   
                v+=1
            else:
                self._prePros[lastLet]['']=1


    def nextChar(self):
        """Generate and return an additional character, given current state."""
        #makes empty list to store previous values 
        prevLetter=[]
        #Count adds one to itself when this function is called
        self._nextCharCount+=1
        #if statmetns that determine how big our counter is and predicts what the next letter will be, appends it to prevList
        if len(self._source)> self._nextCharCount > self._k:
            
            items=self._prePros[prevLetter[self._nextCharCount-3:self._nextCharCount-2]]
            w=random.choice([x for x in items for y in range(items[x])])
            prevLetter.append(w)
            return prevLetter[self._nextCharCount-1]
        if self._nextCharCount <= self._k:
            return self._source[self._nextCharCount-1]
            prevLetter.append(self._source[self._nextCharCount-1])
        if self._nextCharCount==len(self._source):
            prevLetter.append('')
            return '' 




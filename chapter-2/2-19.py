from Progression import Progression

class ArithmeticProgression(Progression):
    def __init__(self, increment=1, start=0):
        super().__init__(start)
        self._increment = increment
    def _advance(self):
        self._current += self._increment

arithProg = ArithmeticProgression(120, 0)
counter = 0

# Note: I used 2**25 because 2**63 takes WAY too long.  Maybe that was part of the challenge
# but I don't see any way around it as of now

while arithProg._current < (2**25):
    arithProg._advance();
    counter += 1

print(counter)


class Progression(object):
    def __init__(self, start=0):
        self._current = start

    def _advance(self):
        self._current += 1

    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        return self

    def print_progression(self, n):
        print(' '.join(str(next(self)) for j in range(n)))




class FibonacciProgression(Progression):
    def __init__(self, first=0, second=1):
        super(FibonacciProgression, self).__init__(first)
        self._prev = second - first

    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        return self

    def _advance(self):
        self._prev, self._current = self._current, self._prev + self._current





fib = FibonacciProgression(2, 2)
fib.print_progression(8)


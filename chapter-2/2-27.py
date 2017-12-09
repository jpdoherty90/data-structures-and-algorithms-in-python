class Range:
    def __init__(self, start, stop=None, step=1):
        if step == 0:
            raise ValueError('step cannot be 0')
        if stop is None:
            start, stop = 0, start
        self._length = max(0, (stop - start + step -1)//step)
        self._start = start
        self._stop = stop
        self._step = step

    def __len__(self):
        return self._length

    def __getitem__(self, k):
        if k < 0:
            k += len(self)
        if not 0 <= k < self._length:
            raise IndexError('index out of range')
        return self._start + k * self._step

    def __contains__(self, k):
        if k >= self._start and k < self._stop and (k - self._start) % self._step == 0:
            return True



myRange = Range(1, 100, 3)
print(7 in myRange)
print(20 in myRange)
        


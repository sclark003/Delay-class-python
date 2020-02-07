import numpy as np

class Delay:
    def __init__(self,n):
        self.n = n
        self.buffer = np.zeros(n)
                
    def delay(self,x):
        l = int(len(x))
        for i in range(l):
            self.buffer = np.append(self.buffer,x[i])
        a = self.buffer[0:l]
        self.buffer = self.buffer[(l):]
        return a



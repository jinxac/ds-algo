class MovingAverage:

    '''
        Check: Double ended queue approach
    '''
    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.temp = []        
        self.size = size
        self.sum = 0
        

    def next(self, val: int) -> float:
        if len(self.temp) == self.size:
            self.sum -= self.temp[0]
            self.temp = self.temp[1:]
        
        
        self.temp.append(val)
        self.sum += val
            
        return self.sum / len(self.temp)
        
        
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

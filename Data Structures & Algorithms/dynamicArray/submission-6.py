class DynamicArray:
    
    def __init__(self, capacity: int):
        if capacity:
            self.size = capacity
            self.array = []

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        #if i < self.size:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.size <= len(self.array):
            self.size *= 2
        self.array.append(n)


    def popback(self) -> int:
        if self.array:
            return self.array.pop()
 
    def resize(self) -> None:
        self.size *= 2 
        
    def getSize(self) -> int:
        return len(self.array)
    
    def getCapacity(self) -> int:
        return self.size

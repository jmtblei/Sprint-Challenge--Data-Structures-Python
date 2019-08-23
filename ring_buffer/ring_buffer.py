class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    #add elements to buffer
    #when the buffer is full, add the newest element and overwrite the oldest

    #check capacity to current
    if self.current >= len(self.storage):
      #reset current to the start of the list if full
      self.current = 0
    self.storage[self.current] = item
    self.current +=1

  def get(self):
    #dont return None values
    return [i for i in self.storage if i is not None]
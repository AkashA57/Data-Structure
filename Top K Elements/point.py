class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
  
    # Overiding __lt__ method to set custom criteria for comparision
    def __lt__(self, other):
        return self.distance_to_origin()>other.distance_to_origin()

    # Using cartesian plane distance formula (ignoring the square root)
    def distance_to_origin(self):
        return self.x*self.x+self.y*self.y
    

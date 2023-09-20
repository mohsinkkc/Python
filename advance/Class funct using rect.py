class Rectangle (): 
    def __init__(self,x = 0,y = 0): 
        self.x = x 
        self.y = y 
    def area (self): 
        return (self.x * self.y) 
rec1=Rectangle(6,10) 
print ("Area is:", rec1.area()) 

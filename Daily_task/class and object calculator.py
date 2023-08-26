class Cal:
    def add(self):
        self.n1=int(input("enter the number 1:"))
        self.n2=int(input("enter the number 2:"))
        return self.n1+self.n2
    def sub(self):
        return self.n1-self.n2
    def mul(self):
        return self.n1*self.n2

ob1=Cal()
print("the addition is :",ob1.add())
print("the sub is :",ob1.sub())
print("the multiplication is :",ob1.mul())

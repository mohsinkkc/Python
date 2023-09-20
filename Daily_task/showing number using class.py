class mynumber:
	def __init__(self, value):
		self.value = value
	
	def new(self):
		print(self.value)

obj1 = mynumber(17)
print("the number is",obj1.new())

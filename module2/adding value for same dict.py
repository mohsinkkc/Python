
dict1 = {'a': 300, 'b': 200, 'c': 100}
dict2 = {'b': 100, 'c': 200, 'a': 300}


for key in dict2:
	if key in dict1:
		dict2[key] = dict2[key] + dict1[key]
	else:
		pass
		
print(dict2)

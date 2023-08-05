# formated string

#  f : f'' or f""
# .format() : str.format(var)

#NOTE:"every thing in python is an object"

#Variable Declaration : container
# In python no need of var declaration

#eg: var_name = 78 

'''

    Keyword : a name that convey special meaning in programming 

    Rules to define variables :


    1. can be form only with alphabet,number or undescore(_)
    2. never contain any spaces
        eg : my var=90 <--x  right :--> my_var=90
    3. var name never same as inbuilt keyword
    4. var name are case sensitive
        eg : Age=67,age=43,AGE=90(all these three are diff var name)
    
'''

#static var: a variable which value is fixed or pre-defined 
name="Mirali"
age=45

print("========simple snippets=====")
print("Your age is : ",age,end=' & ')
print("Your name is : ",name)


print("============with formated string : f''==========")
print(f'Your age is : {age} & Your name is : {name}')


print("===========with .format() method==============")
print("Your age is : {1} & Your name is : {0}".format(name,age))
#.format() is indexible
# the index will starts from zero










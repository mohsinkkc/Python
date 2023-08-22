d1={'what is the come after d':'e',
    'how many days in a week':'7',
    'how many letters in a alphabet':'26',
    'what is 2+5':'7'}

score=0
print("score=",score)


for i,j in d1.items():
    print(i)
    ans=input("enter your answer:")
    if ans==j:
        print("the answer is correct")
        score+=5
       
    else:
        print("your ans is wrong")
        score-=10
        print("score is:",score)
    
    

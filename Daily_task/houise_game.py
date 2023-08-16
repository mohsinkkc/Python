import random

l1=[98,32,65,25,236,56,45,21,455,69,5,8,3,4]
computer=[98,32,65,25,236,56,45]
player=[21,455,69,5,8,3,4]
print("the computer number :",computer)
print("the player number is :",player)


random.shuffle(l1)
print(l1)

for i in l1:
    print(i)
    if i in computer:
        computer.remove(i)
        if len(computer)==0:
            print("Computer win")
            break
    else:
        player.remove(i)
        if len(player)==0:
            print("Player win")
            break

    print("Computer List : ",computer)
    print("Player list : ",player)

    

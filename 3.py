print("select your ride: ")
print("1. bike")
print("2. car")


choice = int( input("enter your choice:  "))


if( choice == 1):
    print("what time of bike? ")
    print("1. scooty\n")
    print("2.scooter\n")

    choice2=int(input("enter your choice2:  "))
    if choice2==1:
        print("you have selected scooty")
    else:
        print("you have selected scooter")

    
elif( choice == 2):
    print("you have selected car")
    print("what type of car?")
    print("1.sudan")
    print("2.suv")
    choice3=int(input("enter your choice3:  "))

    if choice3==1:
        print("you have selected sudan")
    else:
        print("you have selected suv")
else:
    print("Wrong choice!!!")
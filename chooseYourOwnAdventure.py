name = input("Type your name :")
print("welcome",name ,"to this adventure!......")


answer = input("You are on a dirt road , it has come to an end and you can go left or right ..which way would you like to go ").lower()



if answer == "left":
    answer = input("you come to a river ,you can walk around it or swim across ? Type walk to walk around and swim to swim across ").lower()

    if answer == "swim":
        print("You swam across and  were eaten by a alligator .")
    elif answer == "walk":
        print("You walked for many miles and run outof water and you lost...")

    else:
        print("Not a valid option. You lose")
    

elif answer =="right":
     answer == input("You come to a bridge , it look wobbly, do you want to cross it or head back (cross/back) ?").lower()
     if answer == "back":
        print("You go back to the main road .Now you can decide to go back home..")
     elif answer == "cross":
        print("You cross the bridge and meeet the stranger .Do you want to talk to them..(yes/no)").lower()

        if answer == "yes":
            print("You talk to the stranger  and you find solution and got the prize golden coin and win the game !!!")


        elif answer =="no":
            print("you ignore the stranger and they are offended and you lose ... :(")


        else:
            print("no , a valid option you lose ..")

     else:
        print("Not a valid option. You lose")
   
else:
    print("no a valid option .you lose..")

print("Thank you for trying ",name,"!!...")


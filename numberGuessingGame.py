import random
top_of_range = input("type a number :")

g = 0
if  top_of_range.isdigit():
    top_of_range = int(top_of_range)



    if top_of_range <= 0:
        print("please type a number larger than 0 next time.")
        quit()
else:
    print("please type a number next time.")
    quit()


random_number  = random.randint(0,top_of_range)

#number eleven does not be used.
while True :
    g +=1
    user_guess = input("make a guess :")
    
    if user_guess.isdigit():
        user_guess = int (user_guess)
    else:
        print("Please tyoe a number next time .")
        continue

    if user_guess == random_number:
        print("you got it!")
        break
    else:
        if user_guess >random_number:
            print("you aare above the number!")
        else:
            print("you are the below the number.")

print("you got it in", g ,"guesses")
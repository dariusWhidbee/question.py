# Fix Errors

# Variables
corr = 0
q1r = False 
q1a = 3

# Introduction, asks the user 1 question
print(" Hello, this program only runs one question. All you have to do is"
      " choose one of the options below that you think is right")
print()
print("""What object has teeth but can't bite?

1) A zipper
2) A saw
3) A comb
4) A fork""")

# While loop
while q1r == False:
    try:    
        q1a = int(input("Choose the wisely. > "))
         # correct answer "3"
        if q1a == 3:
            corr += 1
            # if the user answers the question right the boolean turns true
            # and gets out of the while loop
            q1r = True
        elif 0 < q1a < 5:
            q1r = True
            # If the user doesn't respond with a interger between 1 to 4
        else:
            print("please choose an interger from 1 to 4")
            # If the user doesn't respond with a interger
    except ValueError:
         print("Invalid response.Please choose either option 1, 2, 3 or 4")
print()
print("You've got", corr * 100,"% out of 100")

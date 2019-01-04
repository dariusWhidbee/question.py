# Add Variables, question and response
# Add comments

# Variables
correct = 0
qla = False 
qlr = 3

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
while qla == False:
    try:    
        qlr = int(input("Choose the wisely. > "))
         # correct answer "3"
        if qlr == 3:
            correct = correct + 1
            print("Exactly 3 is correct. Things like a saw, "
                  "zipper and fork could 'bite' you")
            # if the user answers the question right the boolean turns true
            # and gets out of the while loop
            qla = True
        elif 0 < qlr < 5:
            qlr = True
            # If the user doesn't respond with a interger between 1 to 4
        else:
            print("please choose an interger from 1 to 4")
            # If the user doesn't respond with a interger
    except ValueError:
         print("Invalid response.Please choose either 1, 2, 3 or 4")

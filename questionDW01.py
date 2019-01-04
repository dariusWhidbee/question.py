# Add Variables, question and response

# variable
correct = 0
qla = False 
qlr = 3

# question
print("""What object has teeth but can't bite?

1) A zipper
2) A saw
3) A comb
4) A fork""")

while qla == False:
    try:
        qlr = int(input("Choose the wisely. > "))

        if qlr == 3:
            correct = correct + 1
            print("Exactly 3 is correct. Things like a saw, "
                  "zipper and fork could 'bite' you")
            qla = True
        elif 0 < qlr < 5:
            qlr = True
        else:
            print("please choose an interger from 1 to 4")
    except ValueError:
         print("Invalid response.")

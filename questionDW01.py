while qla == False:
    try:
        qlr = int(input("Choose the wisely. > "))

        if qlr == 3:
            correct = correct + 1
            qla = True
        elif 0 < qlr < 5:
            qlr = True
        else:
            print("please choose an interger from 1 to 4")
        except ValueError:
            print("Invalid response.Please re-run the program and read"
                  "the question carefully")

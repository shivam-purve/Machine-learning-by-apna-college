

#continous input

string = "Quit"
num = input("enter any positive or negative integer continously: ")


while(num != string):
    print(num)
    num = input("enter any positive or negative integer again: ")
    if(num == "Quit"):
        print("you entered Quit!!")

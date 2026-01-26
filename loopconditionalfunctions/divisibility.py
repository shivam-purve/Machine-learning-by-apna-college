# divisibilit by 3 and 5


def divisible_3and5(n):
    for i in range(1,n+1):
        if(i % 15==0):
            print(i)


#fun call

n = int(input("enter number: "))

divisible_3and5(n)
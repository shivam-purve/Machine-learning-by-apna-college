#sum of digits

def sum_digit(n):
    sum = 0
    while(n>0):
        sum += (n%10)
        n //= 10    #integer division
    

    return sum



# fun call

n = int(input("enter a number: "))
digit_sum = sum_digit(n)

print("sum of digits of given number is: ",digit_sum)
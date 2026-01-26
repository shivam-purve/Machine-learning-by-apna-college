#digits of a number






def digits_num(n):
    n = abs(n)
    if n == 0:
        print(0)
        return 1
    

    count = 0
    while(n>0):
        last_dig = n%10
        print(last_dig)
        count += 1
        n //= 10  #integer division
    return count


n = int(input("enter a number: "))
count_dig = digits_num(n)

print("the counts of digits in number is: ",count_dig)

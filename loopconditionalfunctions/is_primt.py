#chekc prime or not

def is_prime(n):
    n = abs(n)
    if(n<3):
        return True
    i = 2
    while(i*i <= n):
        if(n %i == 0):
            return False
        i += 1
        
    return True


#fun call

n = int(input("enter number: "))
if(is_prime(n)):
    print("given number is prime")
else:
    print("given number isnt prime")
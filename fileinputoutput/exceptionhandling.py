

try:
    x = int(input("Enter a number: "))
    ans = 10/x

except ZeroDivisionError:
    print(f"Divide by Zero isnt allowed")

except ValueError:
    print(f"invalid input")
else:
    print(f"ans  = {ans}")
finally:
    print("End of programme")
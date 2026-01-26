#palindrome check

str = input("enter a string: ")
rev_str = ""

for ch in str:
    rev_str = ch + rev_str

if(str == rev_str):
    print(f"{str} is palindrome")
else:
    print(f"{str} is not palindrome")
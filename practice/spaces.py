

str = input("enter string: ")
cnt = 0

for ch in str:
    if(ch == " "):
        cnt += 1

print(f"count of spaces in string {str} is {cnt}")
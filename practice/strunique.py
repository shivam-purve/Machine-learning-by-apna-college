#unique string


def freq(str,ch):
    cnt = 0
    for charval in str:
        if(charval == ch):
            cnt +=1
    
    return cnt

def count_unique(str):
    cnt = 0
    for ch in str:
        if(freq(str,ch) == 1):
            cnt += 1
    
    return cnt



# main

str = input("enter a string: ")
for ch in str:
    if(freq(str,ch) == 1):
        print(f"{ch} ")

print(f"count of unique characters is {count_unique(str)}")
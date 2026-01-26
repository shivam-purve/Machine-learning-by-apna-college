with open("./filehandlingassignemnt/names.txt", "w") as file:
    n = 5
    while n > 0:
        name = input("enter a name: ")
        file.write(name + "\n")
        n -= 1

with open("./filehandlingassignemnt/names.txt", "r") as f:
    for name in f:
        print(name.strip())

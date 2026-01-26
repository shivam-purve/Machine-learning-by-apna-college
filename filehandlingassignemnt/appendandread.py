with open("filehandlingassignemnt/log.txt","a") as f:
    f.write("program ran successfully\n")


with open("filehandlingassignemnt/log.txt","r") as f:
    data = f.read()
    print(data)
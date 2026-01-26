data = True
line = 1
word = "python"

with open("./fileinputoutput/sample2.txt", "r") as f:

    while data:
        data = f.readline()

        if not data:      # ✅ stop at end of file
            break

        if "python" in data:
            print(f"{word} found at line {line}")
            break
        line += 1

       # print(data, end="")

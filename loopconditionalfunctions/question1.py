#conditional statemnt

salary = int(input("enter salary: "))

if(salary < 30000):
    rate = 5
elif(salary<=70000):
    rate = 15
else:
    rate = 25

print("rate according to salary is: ",rate,"%")
# Batting Strike rate calculator
# Batting (s/r) - Avg number of runs scored per 100 balls.

name = input("Enter the name of the batsman: ")
r = input("Enter the runs scored by batsman: ")
r = int(r)
b = input("Enter the number of balls faced by batsman: ")
b = int(b)
avg = r / b
Sr = avg * 100
print("The Strike rate of batsman is : ",name,"is", Sr)

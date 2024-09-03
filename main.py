n=int(input("Enter a number of rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("@", end="")
    print()

for i in range(1,25):
    print("105+%d=%d" %(i,105+i))


for i in range(1,10):
    print("350/%d=%d" %(i,350/i))
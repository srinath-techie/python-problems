# Number Pattern Printer

rows = int(input("Enter the number of rows: "))
print("\nNumber Pattern:\n")
for i in range(1, rows + 1):  
    for j in range(1, i + 1):
        print(j, end=" ")
    print() 

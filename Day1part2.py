# Initialize two empty lists
column1 = []
column2 = []

# Open the text file
with open('input.txt', 'r') as file:
    # Iterate through each line in the file
    for line in file:
        # Split the line into two parts
        num1, num2 = line.split()
        # Append the numbers to the respective lists
        column1.append(int(num1))  # Convert to float or int as needed
        column2.append(int(num2))  # Convert to float or int as needed

# Now column1 and column2 contain the values from the file
column1 = sorted(column1)
column2 = sorted(column2)

sum = 0
for i in range(1000):
    count = 0
    for j in range(1000):
        if column1[i] == column2[j]:
            count += 1
    sum = (column1[i] * count) + sum

print(sum)

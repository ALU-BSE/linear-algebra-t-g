# Initializing Example arrays
Prices = [[300, 500],
          [1000, 120.85]]

Array2 = [200, 100]

# Initializing an empty list to store the result
Ans = []
# (300*200 + 500*100) as an example calculation

# Calculating the Results
for i in range(len(Prices)):
    row_sum = 0
    for j in range(len(Prices[0])):
        # For each element in the array, multiply it by the corresponding element in the second array
        # and add it to the row_sum
        row_sum += Prices[i][j]*Array2[j]
        pass
    # Append the row_sum to the answer array
    Ans.append(row_sum)
    
#Printing the result
print(Ans)

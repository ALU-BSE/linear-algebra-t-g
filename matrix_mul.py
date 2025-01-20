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
        row_sum += Prices[i][j]*Array2[j]
        pass
    Ans.append(row_sum)
    
#Printing the result
print(Ans)

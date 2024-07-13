def diagonalDifference(matrix):
  primary_diagonal_sum=0
  secondary_diagonal_sum=0
  a=len(matrix)
  for i in range(a):
    primary_diagonal_sum+=matrix[i][i]
    secondary_diagonal_sum+=matrix[i][a-i-1]
  return abs(primary_diagonal_sum-secondary_diagonal_sum)

n=int(input())  # Enter the matrix size
matrix=[]
for i in range(n):
  row=list(map(int,input().split())) # Enter the rows
  matrix.append(row)
result= diagonalDifference(matrix)
print(result)

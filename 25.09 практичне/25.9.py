n = int(input())
k = int(input())
matrix = []
for i in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)
row_sums = []
for row in matrix:
    row_sums.append(sum(row))
col_sums = []
for col in range(k):
    col_sum = 0
    for row in range(n):
        col_sum += matrix[row][col]
    col_sums.append(col_sum)
print(row_sums)
print(col_sums)
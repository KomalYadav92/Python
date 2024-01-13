number_grid=[
    [1,4,5],
    [2,3,4],
    [3,4,5],
    [0]
]

print(number_grid[0][0])
print(number_grid[2][2])

#print this nested loop using for loop
for row in number_grid:
    print(row)


for row in number_grid:
    for a in row:
        print(a)
mat1 = [[1,2,3],[4,5,6],[7,8,9]]
mat2 = [[9,8,7],[6,5,4],[3,2,1]]

answer = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(3):
    for j in range(3):
        for k in range(3):
            answer[i][j] += mat1[i][k] * mat2[k][j]

for row in answer:
    print(row)
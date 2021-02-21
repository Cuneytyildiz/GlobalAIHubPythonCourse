"""
Generating a 3x3 matrix with 9 random prime numbers. (You have to do it using the for loop. )
"""
import random

matrix = []

for i in range(3):

    rows = []
    count = 0

    while(count != 3):
        number = random.randint(2,100)
        flag = True
        for d in range(2,number):
            if number % d == 0:
                flag = False
                break
        if flag == True: 
            rows.append(number)
            count += 1
                
    matrix.append(rows)


for i in range(3):
    for j in range(3):
        print(matrix[i][j],end=" ")
    print()

    


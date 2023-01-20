#Name: Bailey Brumfield
#Date: 1/19/2023
#Professor: Juan Parra
#Asignment: Intro Assignment

#import packages
import numpy as np

#define matrix function using arrays
def matrix_array():
    array = np.array([[0,0,0],[0,0,0],[0,0,0]])

    #for matrix 1
    for i in range(0, 3):
        for j in range(0, 3):
            if i == j:
                array[i][j] = 1
            else:
                array[i][j] = 0

    #print formatted matrix 1 and add new line
    print(str(array).replace(' [', '').replace('[', '').replace(']', ''))
    print("\n")
     
     #for matrix 2
    for i in range(0, 3):
        for j in range(0, 3):
            if i == j:
                array[i][j] = 1
            else:
                array[i][j] = 3

    #print formatted matrix 2 and add new line
    print(str(array).replace(' [', '').replace('[', '').replace(']', ''))
    print("\n")

    #print formatted matrix 3 by deleting the last column
    array = np.delete(array, 2, 1)
    print(str(array).replace(' [', '').replace('[', '').replace(']', ''))

#run function
matrix_array()

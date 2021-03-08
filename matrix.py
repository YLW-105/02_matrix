"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    cheese = ''
    for x in matrix:
        for y in x:
            cheese = cheese + str(float(y)) + ' '
        cheese = cheese + "\n"
    print(cheese)

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    for x in range(len(matrix)):
        for y in range(len(matrix)):
            if x==y:
                matrix[x][y] = 1
            else:
                matrix[x][y] = 0

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):

    #new matrix
    matri = new_matrix(rows = len(m2), cols = len(m2[0]))

    #finding the numbers
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                matri[i][j] = matri[i][j] + (m1[i][k] * m2[k][j])

    #replacing m2 numbers
    for x in range(len(matri)):
        for y in range(len(matri[0])):
            m2[x][y] = matri[x][y]

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( rows ):
        m.append( [] )
        for r in range( cols ):
            m[c].append( 0 )
    return m

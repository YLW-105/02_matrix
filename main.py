from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 211, 141, 80 ]
matrix = new_matrix()

print("Testing add_edge. Adding (1, 2, 3), (4, 5, 6) m2 =")
m2 = new_matrix(rows=4, cols=0)
add_edge(m2, 1, 2, 3, 4, 5, 6)
print_matrix(m2)

print("Testing ident. m1 =")
m1 = new_matrix()
ident(m1)
print_matrix(m1)

print('Testing matrix mult. m1 * m2 = ')
matrix_mult(m1, m2)
print_matrix(m2)

print("Testing Matrix mult. m1 =")
m1 = new_matrix(rows=4, cols=0)
add_edge(m1,1,2,3,4,5,6)
add_edge(m1,7,8,9,10,11,12)
print_matrix(m1)

print("Testing Matrix mult. m1 * m2 =")
matrix_mult(m1, m2)
print_matrix(m2)

#IMAGE
joey = new_matrix(rows=4, cols=0)

#TAIL
add_edge(joey, 480, 70, 0, 300, 60, 0)
add_edge(joey, 300, 60, 0, 325, 125, 0)
add_edge(joey, 480, 70, 0, 325, 125, 0)
add_edge(joey, 325, 125, 0, 275, 300, 0)
add_edge(joey, 300, 60, 0, 265, 115, 0)

#LEG
add_edge(joey, 275, 300, 0, 280, 150, 0)
add_edge(joey, 280, 150, 0, 220, 25, 0)
add_edge(joey, 220, 25, 0, 170, 225, 0)
add_edge(joey, 275, 300, 0, 170, 225, 0)
add_edge(joey, 220, 25, 0, 280, 150, 0)
add_edge(joey, 220, 25, 0, 120, 30, 0)
add_edge(joey, 210, 70, 0, 120, 30, 0)
add_edge(joey, 280, 150, 0, 170, 225, 0)

#OTHER LEG
add_edge(joey, 195, 75, 0, 183, 175, 0)
add_edge(joey, 195, 75, 0, 205, 85, 0)
add_edge(joey, 195, 75, 0, 105, 75, 0)
add_edge(joey, 190, 110, 0, 105, 75, 0)

#BODY
add_edge(joey, 125, 250, 0, 183, 175, 0)
add_edge(joey, 125, 250, 0, 150, 325, 0)
add_edge(joey, 275, 300, 0, 150, 325, 0)

#ARM
add_edge(joey, 125, 250, 0, 95, 160, 0)
add_edge(joey, 157, 207, 0, 95, 160, 0)

#NECK
add_edge(joey, 125, 250, 0, 100, 400, 0)
add_edge(joey, 150, 325, 0, 135, 390, 0)
add_edge(joey, 100, 400, 0, 135, 390, 0)

#EAR
add_edge(joey, 100, 400, 0, 135, 390, 0)
add_edge(joey, 135, 390, 0, 105, 425, 0)
add_edge(joey, 105, 425, 0, 75, 445, 0)
add_edge(joey, 100, 400, 0, 75, 445, 0)

#OTHER EAR
add_edge(joey, 135, 390, 0, 140, 410, 0)
add_edge(joey, 105, 425, 0, 140, 410, 0)
add_edge(joey, 105, 425, 0, 80, 455, 0)
add_edge(joey, 90, 434, 0, 80, 455, 0)

#HEAD
add_edge(joey, 105, 370, 0, 25, 350, 0)
add_edge(joey, 20, 370, 0, 25, 350, 0)
add_edge(joey, 20, 370, 0, 85, 425, 0)

draw_lines( joey, screen, color )
display(screen)
"""
Ejercicio python_desde_cero_2024
Programmer: KevMJ

!Se reciben como datos las coordenadas de los puntos P1, P2, P3, que corresponde a los vértices de un triangulo. Desarrolla un algoritmo para calcular e imprimir su perímetro.
>>>
"""

import math

# Inputs 
p1 = input("enter the p1 cordenates as x,y ")
p2 = input("enter the p1 cordenates as x,y ")
p3 = input("enter the p1 cordenates as x,y ")

# Program
p1_x_y = p1.split(",") #Spliting the input to get a tuple with the coordenates
# Converting the tuple to floats and assigning to individual variables
p1_x = float(p1_x_y[0]) 
p1_y = float(p1_x_y[1])

p2_x_y = p2.split(",")
p2_x = float(p2_x_y[0])
p2_y = float(p2_x_y[1])

p3_x_y = p3.split(",")
p3_x = float(p3_x_y[0])
p3_y = float(p3_x_y[1])

"""
The formula to calculate the distance between two dots (points) in a two-dimensional plane (like a graph) is:

d = √((x2 - x1)² + (y2 - y1)²)

where:

d represents the distance between the two points.
(x1, y1) represents the coordinates of the first point.
(x2, y2) represents the coordinates of the second point.
√ represents the square root symbol.
"""
# Calculate line lenghts by finding distances between points
distance_p1_p2 =  math.sqrt((p2_x - p1_x)**2 +(p2_y-p1_y)**2) 
distance_p2_p3 =  math.sqrt((p3_x - p2_x)**2 +(p3_y-p2_y)**2) 
distance_p3_p1 =  math.sqrt((p1_x - p3_x)**2 +(p1_y-p3_y)**2)

# Perimeter of a triangle is just the sum of its three sides
perimeter = distance_p1_p2 + distance_p2_p3 + distance_p3_p1

# Outputs

print(f"The perimeter of the triangle is: {perimeter:.2f}")
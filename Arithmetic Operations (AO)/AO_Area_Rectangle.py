print("Area of a Rectangle Solver")
print("Description: Solves the area of a rectangle")

#input function | type: float | length
length = float(input("Enter the length of your rectangle: "))

#input function | type: float | width
width = float(input("Enter the width of your rectangle: "))

#operation | l * w = area
area = length * width

#print function | f-string | {area}
print(f"The area of your rectangle is {area}")

# write a program that calculates the area of a rectangle

#functon that describes our rectangle builder
def rect_area(width,height):
    return width * height

width = float(input('Enter width: '))
height = float(input('Enter height: '))

area = rect_area(width, height)
print(f'Area: {area:.1f}')



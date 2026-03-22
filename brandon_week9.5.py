# write a program that calculates the area of a rectangle

#functon that describes our rectangle builder
def rect_area(width,height):
    area = width * height
    print(f'Area: {area}')

rect_area(float(input('Width: ')), float(input('Height: ')))


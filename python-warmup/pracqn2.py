#area of rectangle function
def area_rect(width,height):
    area = width * height
    return f"Area = {area}"

print(area_rect(10,20))

#even number list
numbers = [1,2,3,4,5,6,7,8,9,10]
def even_number(numbers):
    even_list = [num for num in numbers if num%2 ==0]
    return f"even number list {even_list}"
print(even_number(numbers))

#TRY/EXCEPT
try:
    input = int(2.1)
    print("Input is integer")
except ValueError:
    print("Input is not an integer")

    
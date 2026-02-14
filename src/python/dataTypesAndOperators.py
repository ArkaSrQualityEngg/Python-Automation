# Implicit and Explicit Type Conversion

# Implicit type conversion is done automatically by the Python interpreter
x= 10
y= 12.9
print("Data type of x is : ",type(x))
print("Data type of y is : ",type(y))

print("Sum of x and y is :", x+y)

#Explicit type conversion
a = 4
b = "45"
b_changed = int(b)
print("Sum of a and b is : ", a+b_changed)
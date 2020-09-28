course = "Python Programming"
print(len(course))  # number of character in this string
print(course[0])  # to get the first character
print(course[-1])  # to get last character
print(course[0:3])  # to get first 3 character
print(course[:3]) #same as before
print(course[0:]) #entire string
print(course[:]) #same as before

#string are immutable,let's verify this
print(id(course))
print(id(course[0]))


 


"""in python we have two types of variable
local variable in the function scope,global vaiable in the file scope"""

message = "a"


def greet():
    global message
    message = "b"


greet()
print(message)

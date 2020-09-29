def multiply(*list):
    # print(list)
    total = 1
    for number in list:
        total *= number
    return total


print(multiply(2, 3, 4, 5))
# when add * before perameter,it will consider as tupple

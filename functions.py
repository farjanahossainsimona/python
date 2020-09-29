"""numbers = [1, 2, 3] list
convert list to tupple
numbers = (1, 2, 3)"""


def increment(number: int, by: int = 1) -> tuple:
    # pass
    return (number, number + by)
    #nmber :original
    # number + by : updated


# keyword argument to make code more readable
#print(increment(2, by=3))
print(increment(2))

first = "Sim"
last = "Ona"
# full = first + "" + last  # concatenate
# print(full)
# instead of concatenation it's better to use this approach
full = f"{first} {last} {3+9} {len(last)}"  # formatted strings
print(full)

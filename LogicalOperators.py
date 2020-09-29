"""name = ""
if not name:
    print("Name is empty")""


name = " " after adding space here its not consider as empty 
if not name:
    print("Name is empty") """
# to fix this issue ,simply call strip.
name = " "
if not name.strip():
    print("Name is empty")

age = 22
# if age >= 18 and age < 65:
if 18 <= age < 65:
    print("Eligible")

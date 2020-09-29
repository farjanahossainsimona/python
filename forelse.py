names = ["chim", "ona"]
# found = False#found flag no needed in python
for name in names:
    if name.startswith("s"):
        print("Found")
        # found = True#found flag no needed in python
        break
# if not found:instesd of this just use
else:
    print("Not found")

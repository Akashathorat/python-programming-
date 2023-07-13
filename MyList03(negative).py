marks = [3, 2, 1, "akash", "true"]
print(marks[-3]) # negative index
print(marks[len(marks)-3]) # positive index
print(marks[5-3]) # positive index 
print(marks[2]) # positive index


if "akash" in marks:
    print("yes")
else:
    print("no")
if "ak" in "akash":
    print("yes")



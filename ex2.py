str = input("Insert a string: ")

if len(str) < 2:
    out = ""
else:
    out = str[0:2] + str[len(str) - 2:len(str)]

print("The result string is:", out)
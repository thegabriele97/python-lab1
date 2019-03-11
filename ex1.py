import sys

while True:
    n1 = input("First number: ")
    n2 = input("Second number: ")

    if not n1.isdigit() or not n2.isdigit():
        print("Error: invalid input! Try again.\n", file=sys.stderr)
        continue

    print("{} + {} = {}\n".format(n1, n2, int(n1) + int(n2)))
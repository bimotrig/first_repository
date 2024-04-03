inStr = input("Enter a string: ")
outStr = ""

for i in range(len(inStr)-1, -1, -1):
    outStr += inStr[i]

print("Output content backwards: %s" % outStr)

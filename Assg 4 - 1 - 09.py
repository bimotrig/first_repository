inStr, outStr = "Python", ""
strLen = len(inStr)

for i in range(0, strLen):
    outStr = inStr[i] + outStr
    print("output content backwards ->> %s" % outStr)


infp = open("C/windows/win.ini", "r")
outfp = open("C/temp/data.txt", "w")

inList = infp.readlines()  # Fill in the blank to read all lines from the input file
for inStr in inList:
    outfp.write(inStr)  # Fill in the blank to write each line to the output file

infp.close()
outfp.close()

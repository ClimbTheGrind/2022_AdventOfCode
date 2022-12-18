def star1():
    maximum = 0;
    tempMax = 0;
    print("Reading from input file...")
    inputFile = open('input', 'r')
    for line in inputFile:
        if line == "\n":
            if tempMax > maximum:
                print("new max: " + str(maximum))
                maximum = tempMax
            tempMax = 0;
        else:
            tempMax += int(line)
    print("Endresult: "+ str(maximum))
    inputFile.close()

def star2():
    maxList = [0]
    tempMax = 0
    sum = 0
    print("Reading from input file...")
    inputFile = open('input', 'r')
    for line in inputFile:
        if line == "\n":
            maxList.append(tempMax)
            tempMax = 0
        else:
            tempMax += int(line)
    maxList.sort(reverse = True)
    topThree = maxList[0:3]
    print("Top Three List: "+ str(topThree))
    for i in topThree:
        sum += i
    print("Endresult (Sum of Top Three): " + str(sum))
    inputFile.close()



# star1()
star2()

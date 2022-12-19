def getVal(c):
    if c.isupper():
        return ord(c) - 38
    else:
        return ord(c) - 96


def star1():
    counter = 0

    print("Reading from input file...")
    inputFile = open('input', 'r')

    for line in inputFile:
        # print(line) 
        fullLen = len(line) - 1
        halfLen = (fullLen/2)
        firstHalf = line[:int(halfLen)]
        secHalf = line[int(halfLen):fullLen] 
        # print(firstHalf)
        # print(secHalf)
        # search for dup
        for foo in firstHalf:
            if foo in secHalf:
                counter += getVal(foo)
                break
        
    # print result
    print("Das Ergebnis ist " + str(counter))


def star2():
    print("Reading from input file...")
    inputFile = open('input', 'r')
    counter = 0
    data = [None, None, None]
    i = 0

    for line in inputFile:
        data[i] = line.strip('\n')

        if (i == 2):
            # search in group
            inter = set(data[0]) & set(data[1]) & set(data[2])
            counter += getVal(list(inter)[0])

            # reset
            data = [None, None, None]
            i = 0
        else:
            i += 1

    print(counter)


# star1()
star2()

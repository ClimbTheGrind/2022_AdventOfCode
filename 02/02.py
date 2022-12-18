def star1():
    inputFile = open('input', 'r')
    globalSum = 0
    for line in inputFile:
        if line == "A X\n":
            globalSum += 4
        if line == "A Y\n":
            globalSum += 8
        if line == "A Z\n":
            globalSum += 3
        if line == "B X\n":
            globalSum += 1
        if line == "B Y\n":
            globalSum += 5
        if line == "B Z\n":
            globalSum += 9
        if line == "C X\n":
            globalSum += 7
        if line == "C Y\n":
            globalSum += 2
        if line == "C Z\n":
            globalSum += 6
        else:
            globalSum += 0

    inputFile.close()
    print("Endsumme nach Strategieplan: " + str(globalSum))


def star2():
   
    print('Reading data from input file...')
    inputFile = open('input', 'r')
    globalSum = 0
    X = 'X\n'
    Y = 'Y\n'
    Z = 'Z\n'
    A = 'A'
    B = 'B'
    C = 'C'

   # read input
    for line in inputFile:
        if line.endswith(X):
            # loose
            if line.startswith(A):
                globalSum += 3
            if line.startswith(B):
                globalSum += 1
            if line.startswith(C):
                globalSum += 2
        elif line.endswith(Y):
            # draw
            globalSum = globalSum + 3 + ord(line[:1]) - 64
        elif line.endswith(Z):
            # win
            globalSum += 6
            if line.startswith(A):
                globalSum += 2
            if line.startswith(B):
                globalSum += 3
            if line.startswith(C):
                globalSum += 1
    
    inputFile.close()
    print("Endsumme nach Strategieplan: " + str(globalSum))


star2()

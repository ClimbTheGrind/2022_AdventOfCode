def star1():
    # input datei oeffnen
    inputFile = open('input', 'r')

    # stack
    stack = []
    stackCreationDone = False

    # initialisiere Stack größe
    line = inputFile.readline()
    linesize = len(line)
    print("Unsere Stackgröße ist für " + str(linesize) + " Stapel.") 
    for i in range (0, int(linesize / 4)):
        stack.append([])
    
    print(stack)
    inputFile.close()


    inputFile = open('input', 'r')

    # Zeile fuer Zeile lesen
    for line in inputFile:
        # Abrruchkriterium
        if line in ['\n', '\r\n']:
            stackCreationDone = True
            # drehe stapel um nach dem füllen
            for i in range (0, int(linesize / 4)):
                stack[i].reverse()
            print("Alle Kisten gelesen")

        if stackCreationDone == False:
            # befülle stack mit kisten
            # [x] [y]
            for i in range (1, linesize, 4):
              # print("Stelle in line: %d" %i)
              stapel = int((i - 1) / 4)
              # print(stapel)
              if line[i].isalpha():
                stack[stapel].append(line[i])
              # print(stack)

        if line.startswith('move'):
            res = [int(i) for i in line.split() if i.isdigit()]
            ntimes = res[0]
            fr = res[1]
            to = res[2]
            print("times: %d, from: %d, to: %d" %(ntimes, fr, to))
            print(stack)
            for i in range(0,ntimes):
                stack[to - 1].append(stack[fr - 1].pop())
            print(stack)


    print(stack)
    result = ""
    for stapel in stack:
        result += stapel.pop()
    print(result)


def star2():
    # input datei oeffnen
    inputFile = open('input', 'r')

    # stack
    stack = []
    stackCreationDone = False

    # initialisiere Stack größe
    line = inputFile.readline()
    linesize = len(line)
    print("Unsere Stackgröße ist für " + str(linesize) + " Stapel.") 
    for i in range (0, int(linesize / 4)):
        stack.append([])
    
    print(stack)
    inputFile.close()


    inputFile = open('input', 'r')

    # Zeile fuer Zeile lesen
    for line in inputFile:
        # Abrruchkriterium
        if line in ['\n', '\r\n']:
            stackCreationDone = True
            # drehe stapel um nach dem füllen
            for i in range (0, int(linesize / 4)):
                stack[i].reverse()
            print("Alle Kisten gelesen")

        if stackCreationDone == False:
            # befülle stack mit kisten
            # [x] [y]
            for i in range (1, linesize, 4):
              # print("Stelle in line: %d" %i)
              stapel = int((i - 1) / 4)
              # print(stapel)
              if line[i].isalpha():
                stack[stapel].append(line[i])
              # print(stack)

        if line.startswith('move'):
            res = [int(i) for i in line.split() if i.isdigit()]
            ntimes = res[0]
            fr = res[1]
            to = res[2]
            print("times: %d, from: %d, to: %d" %(ntimes, fr, to))
            print(stack)
            tempStack = []
            # move n crates IN ORDER 
            for i in range(0,ntimes):
                tempStack.append(stack[fr - 1].pop())
            while len(tempStack) > 0:
                stack[to - 1].append(tempStack.pop())
            print(stack)


    print(stack)
    result = ""
    for stapel in stack:
        result += stapel.pop()
    print(result)

#star1()
star2()



'''
1 - 33

minus 1
--> 0 - 32

durch 4

--> 0 - 8

'''


'''
list1 = [1, 2, 3, 4, 5]
print("The first list is:", list1)
list2 = [12, 13, 23]
print("The second list is:", list2)
list3 = [10, 20, 30]
print("The third list is:", list3)
list4 = [11, 22, 33]
print("The fourth list is:", list4)
list5 = [12, 24, 36]
print("The fifth list is:", list5)
print("\n")
myList = []
myList.append(list1)
myList.append(list2)
myList.append(list3)
myList.append(list4)
myList.append(list5)
print("The stack is:")
print(myList)

print("\npop operation:")
print(myList[0])
pop = myList[0].pop()
print(pop)
print("push operation:")
print(myList[1])
myList[1].append(pop)
print("result:")
print(myList[1])
print(myList[0])
'''

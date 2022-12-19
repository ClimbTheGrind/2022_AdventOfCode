def star1():
    # open input here: read line by line
    inputFile = open('input', 'r')

    # intersection counter
    ic = 0

    # cur line
    for line in inputFile:
        line = line.strip('\n')
        # line = "1-50,2-3"
        print(line)

        # elf1
        elf1 = line.split(",")[0]
        print(elf1)
        elf1_from = int(elf1.split("-")[0])
        elf1_to = int(elf1.split("-")[1])
        print(elf1_from)
        print(elf1_to)

        elf1_area = set([*range(elf1_from, elf1_to + 1)])
        print(elf1_area)

        # elf2
        elf2 = line.split(",")[1]
        print(elf2)
        elf2_from = int(elf2.split("-")[0])
        elf2_to = int(elf2.split("-")[1])
        print(elf2_from)
        print(elf2_to)

        elf2_area = set([*range(elf2_from, elf2_to + 1)])
        print(elf2_area)

        # elf1 & elf2 intersect
        inter = elf1_area & elf2_area
        if inter == elf1_area or inter == elf2_area:
            ic += 1

    print(ic)

def star2():
    # open input here: read line by line
    inputFile = open('input', 'r')

    # intersection counter
    ic = 0

    # cur line
    for line in inputFile:
        print("new line:")
        line = line.strip('\n')
        # line = "1-50,2-3"
        print(line)

        # elf1
        elf1 = line.split(",")[0]
        print(elf1)
        elf1_from = int(elf1.split("-")[0])
        elf1_to = int(elf1.split("-")[1])
        print(elf1_from)
        print(elf1_to)

        elf1_area = set([*range(elf1_from, elf1_to + 1)])
        print(elf1_area)

        # elf2
        elf2 = line.split(",")[1]
        print(elf2)
        elf2_from = int(elf2.split("-")[0])
        elf2_to = int(elf2.split("-")[1])
        print(elf2_from)
        print(elf2_to)

        elf2_area = set([*range(elf2_from, elf2_to + 1)])
        print(elf2_area)

        # elf1 & elf2 intersect
        if (elf2_from in elf1_area) or (elf2_to in elf1_area) or(elf1_from in elf2_area) or(elf1_to in elf2_area):
            print("range overlap!")
            ic += 1

        
        print("line finished\n")

    print(ic)


star2()
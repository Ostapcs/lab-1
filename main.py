# global variables
memorySize = 0
width = 0
memory = []


def showHelpMessage():
    print("""
    Available commands:

    help - show this help
    exit - exit this program
    print - print memory blocks map
    allocate <num> - allocate <num> cells. Returns block first cell number
    free <num> - free block with first cell number <num>""")


buff = []


def printFunc():
    # print("Print function")
    vertBar = "|"
    filler = "x"

    # if not memory:
    #     if memorySize % width == 0:
    #         for i in range(int(memorySize / width)):
    #             print(vertBar + "x" * (width - 1) * 2 + vertBar, end="\n")
    #     else:
    #         for j in range(int(memorySize // width)):
    #             print(vertBar + " " * (width - 1) * 2 + vertBar, end="\n")
    #         print(vertBar + "x" * ((int(memorySize % width)) * 2) + vertBar, end="\n")
    # else:
    #     for i in memory:
    #         if i[0] == 0:
    #             print(vertBar + ((i[1] * 2) - 1)  * "x" + vertBar,end="")
    #             if()

    # for i in range(len(memory)):
    #     temp = 0
    #     temp += memory[i][1]
    #     if temp >= 0 and temp != :
    #         str = vertBar + str(memory[i][0]) + filler * (temp * 2 - 1)
    #         buff[0] += str + vertBar
    #         # buff[0] = vertBar + filler * (temp * 2 -1 ) + vertBar + (memorySize * 2 - temp * 2) * " " + vertBar
    #     else:
    #         continue
    #     if (temp > (width + 2)):
    #         print(temp / (width + 2))
    # print(buff[0])
    if not buff:
        if memorySize % width == 0:
            segment = memorySize / width
            for i in range(int(segment)):
                buff.append([vertBar])
                for j in range(width * 2):
                    # if buff[i][0] != vertBar:
                    #     buff[i].append(vertBar)

                    buff[i].append(" ")
        # else:
        #     segment = memorySize // width
        #     remainder = memorySize % width
        #     for i in range(int(segment)):
        #         buff.append(vertBar + " " * width * 2 + vertBar)
        #     buff.append(vertBar + " " * int(remainder) * 2 + vertBar)
    # print(buff[0].split(" "))
    # buff[0] = buff[0].split()
    # for i in range(len(buff[0])):
    #     print(buff[0][i],end="")
    # for i in memory:
    #     for j in
    # print(len(buff[0]))
    # for i in memory:
    #     temp = i[1] * 2
    #     index = 0
    #     for j in range(len(buff)):
    #         for k in range(len(buff[j])):
    #             if buff[j][k] == "x":
    #                 continue
    #             else:
    #                 index = k
    #                 break
    #         # buff[j] = buff[j].replace(buff[j][1:temp], filler * temp + vertBar, 1)
    #         # break
    #
    #     # temp = (
    #     # i[1] * 2)
    #     # old = buff[0][1:temp]
    #     # new = filler * temp
    #     # buff[0] = buff[0].replace(old,new,1) #vertBar + filler * temp  + vertBar + buff[0][temp+1:]
    #
    # print(buff[0])
    # print(buff)
    for i in buff:
        for j in range(len(i)):
            print(i[j],end="")
        print(vertBar,end="\n")
    # print(buff)

def allocate(num):
    # print(num)
    global allocIndex
    if num > memorySize:
        return print("OUT_OF_RANGE")
    elif num <= 0:
        print("""
Cant allocate memory that have size 0 or negativ.
Please enter yout number again.
            """)
    elif not memory:
        allocIndex = 0
        memory.append([allocIndex, num])
        print(allocIndex)
        allocIndex += num
    elif len(memory) >= 1:


        for i in range(len(memory) - 1):
            if memory[i + 1][0] - memory[i][1] != memory[i][0] and num <= memory[i + 1][0] - (
                    memory[i][1] + memory[i][0]):
                memory.insert(i + 1, [memory[i][1] + memory[i][0], num])
                return print(memory[i][1] + memory[i][0])

        else:
            if (memory[-1][0] + memory[-1][1]) + num > memorySize:
                return print("OUT_OF_RANGE")
            memory.append([allocIndex, num])
            print(allocIndex)
            allocIndex = allocIndex + num

        # print(memory)


def free(num):
    # memory.remove(int(num))
    for x in memory:
        if (x[0] == num):
            memory.remove(x)
    print(memory)


isActive = True

while isActive:
    print("Please set memory size and max output width:")
    memorySize, width = input().split(" ")

    memorySize = int(memorySize)
    width = int(width)

    print("Type 'help' for additional info.")

    isHelp = True
    command = str(input())
    while isHelp:
        if command == "help":
            showHelpMessage()
            break
        else:
            command = str(input("Type 'help' for additional info.: "))

    isRightInput = True
    allocIndex = 0
    while len(command) > 0:
        command = str(input("Enter commad : "))
        command = command.split()
        command.append(None)

        if command[0] == "exit":
            isActive = False
            break
        elif command[0] == "print":
            printFunc()
            continue
        elif command[0] == "allocate" and command[1] is not None:
            allocate(int(command[1]))
            continue
        elif command[0] == "free" and command[1] is not None:
            free(int(command[1]))
            continue
        elif command[0] == "help":
            showHelpMessage()
            continue
        else:
            continue

    isActive = False

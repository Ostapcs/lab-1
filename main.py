from functools import reduce
# global variables

memorySize = 0
width = 0
memory = []

print(str(13 // 10) + str(13 % 10))


# розібратися в алокейті коли 10 5 і треба вставити 0 10

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
    # if not buff:
    #     if memorySize % width == 0:
    #         segment = memorySize / width
    #         for i in range(int(segment)):
    #             buff.append([vertBar])
    #             for j in range(width * 2):
    #                 buff[i].append(" ")
    temp = width * 2

    for i in range(memorySize * 2):
        buff.append(" ")
    # for i in range(memorySize * 2 - 1):
    #     if i == temp - 1:
    #         buff.append(" ")
    #         buff.append(vertBar)
    #         buff.append("\n")
    #         buff.append(vertBar)
    #         temp += width * 2
    #     elif i == memorySize * 2 - 2:
    #         buff.append(" ")
    #         buff.append(" ")
    #         buff.append(vertBar)
    #         break
    #     else:
    #         buff.append(" ")
    # if memorySize % width != 0:
    #     buff.append("\n")
    #     buff.append(vertBar)
    #     tail = int(memorySize % width ) * 2
    #     for i in range(tail - 1):
    #         buff.append(" ")
    # Перевірка при видаленні
    # індекс 2 числа
    # for i in memory:
    #     count = i[0] * 2
    #     if count == 0:
    #         buff[count + 1] = i[0]
    #     else:
    #         while buff[count] == filler or buff[count] == vertBar or buff[count] == "\n":
    #             count += 1
    #         buff[count] = i[0]
    #     for j in range(i[1] * 2):
    #         # if buff[count] == vertBar or buff[count] == "\n" or buff[count] == i[0] or buff[count] == filler:
    #         #     # j -= 1
    #         #     count += 1
    #         #     if buff[count] == vertBar or buff[count] == "\n" or buff[count] == i[0]:
    #         #         count += 1
    #         #         if buff[count] == vertBar or buff[count] == "\n" or buff[count] == i[0]:
    #         #             count += 1
    #         #         else:
    #         #             continue
    #         #     else:
    #         #         continue
    #         while buff[count] == vertBar or buff[count] == "\n" or buff[count] == i[0] or buff[count] == filler:
    #             count += 1
    #         else:
    #             buff[count] = filler
    #             if j == (i[1] * 2) - 2:
    #                 if  buff[count + 1] == vertBar or buff[count] == "\n" :
    #                     break
    #                 buff[count] = vertBar
    #                 break
    #             count += 1

    for i in memory:
        count = i[0] * 2
        widthBlock = i[1] * 2 - 1
        if count == 0:
            buff[count] = i[0]
            count += 1

        else:
            if buff[count-1] == " ":
                buff[count-1] = vertBar
            while buff[count] == filler or buff[count] == vertBar or buff[count] == "\n":
                count += 1
            if i[0] >= 10:
                buff[count] = i[0] // 10
                count += 1
                buff[count] = i[0] % 10
                count += 1
                widthBlock -= 1
            else:

                buff[count] = i[0]
                count += 1
        for j in range(widthBlock):
            buff[count] = filler
            if j == (i[1] * 2) - 2 and i[0] < 10:
                buff[count] = vertBar
                break
            elif j == (i[1] * 2) - 3 and i[0] >= 10 and buff[count] != buff[-1]:
                if count % width == 0:
                    buff[count] = filler
                    break
                buff[count] = vertBar
                break
            count += 1

    # temp = width * 2
    # for i in range(memorySize * 2):
    #     if i == temp :
    #         if buff[i] == vertBar:
    #             buff.insert(i+1,"\n")
    #             buff.insert(i + 2, vertBar)
    #             temp += width * 2
    #             continue
    #         else:
    #             buff.insert(i,vertBar)
    #             buff.insert(i+1,"\n")
    #             buff.insert(i+2,vertBar)
    #             temp += width * 2
    #     # elif i == memorySize * 2 - 1:
    #     #     buff.insert(i+1,vertBar)
    #     #     break
    # buff[-1] = vertBar
    #
    count = 0
    temp = width * 2
    for i in range(int(memorySize / width)):
        print(vertBar, end="")
        for j in range(len(buff)):
            if j == width * 2:
                print(vertBar)
                break
            else:
                if count == temp - 1:
                    if buff[count] == vertBar and buff[count - 1] == filler:
                        buff[count] = filler
                    temp += width * 2
                print(buff[count], end="")
                count += 1

    if memorySize % width != 0:
        tail = int(memorySize%width) * 2
        print(vertBar,end="")
        for i in range(tail):
            print(buff[count],end="")
            count += 1
    if memorySize % width != 0:
        print(vertBar)

    # print(buff)
    # print(len(buff))

    buff.clear()


def allocate(num):
    # print(num)
    # global allocIndex
    if num > memorySize:
        return print("OUT_OF_RANGE")
    elif num <= 0:
        print("""
Cant allocate memory that have size 0 or negativ.
Please enter your number again.
            """)
    elif not memory:
        # allocIndex = 0
        memory.append([0, num])
        print(0)
    elif len(memory) >= 1:

        for i in range(len(memory) - 1):
            if memory[i + 1][0] - memory[i][1] != memory[i][0] and num <= memory[i + 1][0] - (
                    memory[i][1] + memory[i][0]) and num >= memory[0][0]:
                memory.insert(i + 1, [memory[i][1] + memory[i][0], num])
                return print(memory[i][1] + memory[i][0])
        else:
            sum = 0
            # sum += num
            # зробити норм перевірку на вихід за масив
            for j in memory:
                sum += j[1]

            if memory[0][0] != 0 and num <= memory[0][0]:
                memory.insert(0, [0, num])
                return print(0)
            # elif sum > memorySize or j[0] > memorySize:
            #     return print("OUT_OF_RANGE")
            elif num > (memorySize - (memory[-1][0] + memory[-1][1])):
                    return print("OUT_OF_RANGE")
            elif num <= memorySize :
                memory.append([memory[-1][1] + memory[-1][0], num])
                return print(memory[-1][0])




            # print(allocIndex)
            # allocIndex = allocIndex + num

    print(memory)


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

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


def printFunc():
    print("Print function")


def allocate(num):
    # print(num)
    global allocIndex
    if num > memorySize:
        return print("OUT_OF_RANGE")
    elif num <=0:
        return print("")
    elif not memory:
        allocIndex = 0
        memory.append([allocIndex, num])
        allocIndex += num
    elif len(memory) >= 1:

        for i in range(len(memory) - 1):
            if memory[i + 1][0] - memory[i][1] != memory[i][0] and num <= memory[i + 1][0] - (
                    memory[i][1] + memory[i][0]):
                memory.insert(i + 1, [memory[i][1] + memory[i][0], num])
                return print(memory)

        else:
            print("sum", (memory[-1][0] + memory[-1][1]) + num)
            if (memory[-1][0] + memory[-1][1]) + num > memorySize:
                return
            memory.append([allocIndex, num])
            allocIndex = allocIndex + num

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

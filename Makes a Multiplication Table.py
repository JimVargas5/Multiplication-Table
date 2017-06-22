import string

def MultTable(AList):
    print("Multiplication table of", AList[-1], '\n')
    count = 1
    for j in range(max(AList)):
        running = ""
        for i in AList:
            New = int(i)*count
            running = str(running)+'\t'+str(New)
        count = count + 1
        print (running)
    #return running


def check():
    print("Do you want to continue?")
    thing = input("Y or N?"+'\n'+">>> ")
    if (thing == "Y") or (thing == "y"):
        main()
    elif (thing == "N") or (thing == "n"):
        print("Quitting...")
        exit()
    elif len(thing) == 0:
        print("You didn't enter anything.")
        print("Quitting...")
        exit()
    elif len(thing) > 1:
        print("The program needs a one letter anser.", '\n')
        check()
    else:
        print("You entered something invalid.")
        print("Quitting...")
    exit()


def main():
    print("This prints a multiplication table. If you enter a number (n), the table will have n rows and columns.",'\n')
    n = input("How big do you want your multiplication table to be?"+'\n'+">>> ")
    if n.isdigit():
        n = int(n)
        if n>15:
            print("That table would be too big.")
            check()
        else:
            List = range(1,(n+1))
            MultTable(List)
    else:
        print("You didn't enter a number.")
        check()


if __name__ == '__main__':
    main()
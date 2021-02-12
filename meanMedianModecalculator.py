numList = []

while True:
    try:
        listnums = int(input("Enter the numbers enter exit to exit\n"))
        numList.append(listnums)
    except Exception as e:
        break

listSize = len(numList)
add = sum(numList)


def mean(sumOfNumbers, sizeOfList):
    return sumOfNumbers/sizeOfList


numListcopy = numList.copy()
numListcopy.sort()


def median(n):
    if n % 2 != 0:
        positionodd = (n+1)//2
        return numListcopy[positionodd-1]
    elif n % 2 == 0:
        positionone = n//2
        positiontwo = (n//2)+1
        observation = (numListcopy[positionone-1] +
                       numListcopy[positiontwo-1])/2
        return observation


def mode(List):
    counter = 0
    num = List[0]

    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency > counter):
            counter = curr_frequency
            num = i
    return num


print(f"Mean of the numbers provided by you = {mean(add,listSize)}")
print(f"Median of the numbers provided by you = {median(listSize)}")
print(f"Mode of the numbers provided by you =  {mode(numList)}")

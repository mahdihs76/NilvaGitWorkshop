def main():
    a,b = int(input()), int(input())
    print(sub(a,b))
    
    myList = input("enter your list: ")
    for i in range(len(myList)):
        myList[i] = int(myList[i])
    print(maximum(myList)

def maximum(myList):
    max = 0
    for i in myList:
        if max < i:
            max = i
    return max

def sub(a,b):
    return a - b
    
main()

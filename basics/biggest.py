firstNum = int(input())
secondNum = int(input())
thirdNum = int(input())

if firstNum > secondNum and firstNum > thirdNum:
    print(firstNum)
elif secondNum > firstNum and secondNum > thirdNum:
    print(secondNum)
else:
    print(thirdNum)


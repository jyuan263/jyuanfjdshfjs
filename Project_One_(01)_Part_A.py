count   = 2
pre1Num = 0
pre2Num = 1
newNum  = 0

# Ask the user sequence end at which number
userInput = int(input("Sequence end at: ")) + 1

# Fibonacci start with 0 and 1
print("0: 0 0")
print("1: 1 1")

while count < userInput:
    # Calculate the new number by adding the previous two numbers
    newNum = pre1Num + pre2Num
    print( str(count) + ": " + str(newNum) + str(f"{newNum: ,}") )
    # Reset the previous number variable.
    pre1Num = pre2Num
    pre2Num = newNum
    count += 1


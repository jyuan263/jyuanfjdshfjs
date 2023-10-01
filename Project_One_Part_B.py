start = int(input("Prime Numbers starting with: "))
end = int(input("and end with: "))

print()

# Inform the user if the input is incorrect, and switch the two input
if end < start:
    print("Incorrect Input: " + str(start) + " is greater than " + str(end))
    print("The numbers have been automatically switched.")
    temp = start
    start = end
    end = temp

print()

print("Prime numbers in the range from : " + str(start) + " and " + str(end) + " are:")

# Loop through the range and check if there are any prime number
for i in range(start, end):
    isPrime = True
    # Try to find if the current number is prime or not
    for j in range(2, i):
        if i % j == 0:
            isPrime = False

    # Print the number if it is a prime number
    if isPrime:
        print(str(i) + " is prime")
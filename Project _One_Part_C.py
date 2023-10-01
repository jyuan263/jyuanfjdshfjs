# Ask for user input
startTran = int(input("Starting Number of transistors: "))
startYear = int(input("Starting Year: "))
totalYear = int(input("Total Number of Years: "))
newTran = startTran

print()

print("YEAR: TRANSISTORS : FLOPS:")

# Loop through the range(start year + total year)
for i in range(startYear, (startYear + int(totalYear) + 2), 2):
    flops = newTran * 50
    decimalFlops = flops
    newFlops = ""

    # Check and choose which unit to use
    if len(str(flops)) < 4:
        newFlops = "FLOPS"
    elif len(str(flops)) < 7:
        decimalFlops = flops / 1000
        newFlops = "kiloFLOPS"
    elif len(str(flops)) < 10:
        decimalFlops = flops / 1000000
        newFlops = "megaFLOPS"
    elif len(str(flops)) < 13:
        decimalFlops = flops / 1000000000
        newFlops = "gigaFLOPS"
    elif len(str(flops)) < 16:
        decimalFlops = flops / 1000000000000
        newFlops = "teraFLOPS"
    elif len(str(flops)) < 19:
        decimalFlops = flops / 1000000000000000
        newFlops = "petaFLOPS"
    elif len(str(flops)) < 22:
        decimalFlops = flops / 1000000000000000000
        newFlops = "exaFLOPS"
    elif len(str(flops)) < 25:
        decimalFlops = flops / 1000000000000000000000
        newFlops = "zettaFLOPS"

    print(str(startYear) + " " + str(f"{newTran: ,}") + " " + "{:.2f}".format(decimalFlops) + " " + str(newFlops) + " " + str(f"{flops: ,}"))

    # Multiply the old transistors with 2 to get new transistor
    newTran = newTran * 2
    # Add 2 to get new year
    startYear += 2
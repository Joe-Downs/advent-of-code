import io

report = []
f = open("puzzleInput.txt", "r")
for number in f:
    report.append(int(number))

def search2020():
    for number in report:
        for factor in report:
            if number + factor == 2020:
                print(f"{number} + {factor} = 2020")
                print(f"{number} * {factor} = {number * factor}")
                return

search2020()

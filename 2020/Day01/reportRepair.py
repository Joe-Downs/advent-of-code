import io

report = []
f = open("puzzleInput.txt", "r")
for number in f:
    report.append(int(number))

def search2020():
    for number in report:
        for factor in report:
            for factor2 in report:
                if number + factor + factor2 == 2020:
                    print(f"{number} + {factor} + {factor2} = 2020")
                    print(f"{number} * {factor} * {factor2} = {number * factor * factor2}")
                    return

search2020()

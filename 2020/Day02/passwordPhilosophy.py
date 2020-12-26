import io

f = open("day02Input.txt", "r")

class PasswordEntry:
    def __init__(self, letter, letterMIN, letterMAX, password):
        self.letter = letter
        self.letterMIN = letterMIN
        self.letterMAX = letterMAX
        self.password = password

    def __str__(self):
        return f"{self.letterMIN}-{self.letterMAX} {self.letter}: {self.password}"

PasswordList = []
    
for line in f:
    val, char, password = line.split(" ")
    letterMIN, letterMAX = val.split("-")
    entry = PasswordEntry(char[0], int(letterMIN), int(letterMAX), password.strip("\n"))
    PasswordList.append(entry)    

f.close()

validCount = 0

for passwordEntry in PasswordList:
    letter = passwordEntry.letter
    count = passwordEntry.password.count(letter)
    if count >= passwordEntry.letterMIN and count <= passwordEntry.letterMAX:
        validCount += 1

print(f"There are {validCount} valid passwords")

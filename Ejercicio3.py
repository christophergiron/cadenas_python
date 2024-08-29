name = input("Enter a name: ")
LetterCount = 0
for Count in name:
    if Count.isalpha():
        LetterCount += 1
print(name.upper(), "have", LetterCount, "letters")

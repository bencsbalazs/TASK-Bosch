def countVowels(word: str) -> int:
    numVowels = 0
    for char in word.lower():
        if char in "aeiou":
            numVowels += 1
    return numVowels


print(countVowels("Celebration"))

import sys
import string

def main():
    words = []
    dic = {}
    blank = False


    for line in sys.stdin:
        line = line.rstrip('\n')

        if len(line.strip()) == 0:
            blank = True
            continue

        if not blank:
            words.append(line.lower())
        else:
            wordLength = len(line)
            if wordLength not in dic:
                dic[wordLength] = []
            dic[wordLength].append(line.lower())
    
    for word in words:
        anagram = findAnagram(word, dic)
        if anagram is None:
            print(f"{word}: ")
        else:
            print(f"{word}: {anagram}")



def findAnagram(word, dic):

    wordlength = len(word)
    letters = countLetters(word)
    dicLargestWord = max(dic.keys())

    if (wordlength > dicLargestWord):
        length = dicLargestWord
    else:
        length = wordlength

    for num in range(length, 1, -1):
        dicList = dic[num]
        for dicWord in dicList:
            dicLetters = countLetters(dicWord)
            if letters == dicLetters:
                return dicWord
            
                

def countLetters(word):
    # Count occurrences of each character in the word
    count = {}
    for char in word:
            count[char] = count.get(char, 0) + 1
    return count

def splitWords(letters, dicLetters):
    leftover_letters = letters.copy() 
    for char, count in dicLetters.items():
        if char not in leftover_letters or leftover_letters[char] < count:
            return None  # Invalid dicLetters, return None
        leftover_letters[char] -= count
    return leftover_letters

    # for char in dicLetters:
    #     if char in letters:
    #         letters[char] = letters.get(char) - 1

main()
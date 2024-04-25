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

    length = len(word)
    letters = countLetters(word)

    for num in range(length, 1, -1):
        dic[num]
    return

def countLetters(word):
    # Count occurrences of each character in the word
    count = {}
    for char in word:
            count[char] = count.get(char, 0) + 1
    return count

main()
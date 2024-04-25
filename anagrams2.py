# Anagrams approach 

# Normalise input, convert words to lowercase and filter out non alphabetic characters 
# filter and isAlpha 

# Count characters for each word - use Counter from collections library 
# Each word is now a tuple containing the word and its character count 

# Once input normalised and characters in ea word counted, sort the list of 
# dicontary words 

# Words sorted in descending order of length so when finding anagrams, 
# longer words are favourited (longer words are better as problem specifies)
# else 
# Words that're the same length are sorted alphabetically 

# Anagram comparison: Compare lists of words based on lengths as longer is better 
# If lengths are equal then compare in alphabetical order 

# Recursively find anagrams. Must find all possible combinations of given 
# dictionary words that match target words char count 

# Recursively subtract the character count of ea dict word from the target words count 
# if this gives positive char count then that word could be anagram 
# Results of computations are instantly stored so all is only computated once 

# Out of these potential anagrams found, a comparison function choses the 'best'

from collections import Counter, defaultdict
import itertools
import sys

def CleanUp(word):
    return ''.join(filter(str.isalpha, word.lower()))

def CharCount(word):
    return Counter(word)

def CompareWords(word1,word2):

    for word1,word2 in itertools.zip_longest(word1,word2,fillvalue=""):

        if len(word1) != len(word2):
            return len(word2) - len(word1)
        if word1 != word2:
            return (word1 > word2) - (word1 < word2)
    return 0

def FindAnagram(goalCharCount, availableWords):

    store = {} 

    def search(count):
        # base case for recursion
        if sum(count.values()) == 0:
            return [] 

        if tuple(count.items()) in store:
            return store[tuple(count.items())]
        
        bestAnagram = None 

        for word, wordCount in availableWords: 

            if all(count[char] >= wordCount[char] for char in wordCount):  
                remainingCount = count - wordCount
                # recursively search with new remaining char count 
                result = search(remainingCount)
                if result is not None: 

                    possibleBest = [word] + result

                    # if current candidate is 'better' than best, make it best
                    if bestAnagram is None or CompareWords(possibleBest, bestAnagram) < 0:
                        bestAnagram = possibleBest
        
        store[tuple(count.items())] = bestAnagram
        
        return bestAnagram 
    # just calls search when FindAnagram called as need to store outside of function
    return search(goalCharCount)

def FindBestAnagrams(words, dictionaryWords):

    # process dictionary and sort by length and alphabetical order
    dictWordsProcessed = [(word, CharCount(word)) for word in map(CleanUp, dictionaryWords) if word]
    dictWordsProcessed.sort(key=lambda x: (-len(x[0]), x[0]))
    
    # process words (in first input block) and find anagrams calling FindAnagram on each word 
    results = [] 

    for word in words: 

        cleanedUpWord = CleanUp(word) 
        wordCount = CharCount(cleanedUpWord) 
        anagram = FindAnagram(wordCount, dictWordsProcessed)
        result = f"{word}: {' '.join(anagram)}" if anagram else f"{word}:"
        results.append(result)
    return results

def FormatAnagram(results):
    return "\n".join(results)

# words = ["apple", "appleapple", "frog"]
# dictionaryWords = ["app", "el", "leap", "pel"]

def main():
    words = []
    dictionaryWords = []
    blank = False


    for line in sys.stdin:
        line = line.rstrip('\n')

        if len(line.strip()) == 0:
            blank = True
            continue

        if not blank:
            words.append(line.lower())
        else:
            dictionaryWords.append(line.lower())
    
    results = FindBestAnagrams(words, dictionaryWords)
    formattedOutput = FormatAnagram(results)
    print(formattedOutput)

main()



from collections import Counter, defaultdict
import sys

def find_anagrams(word, dictionary_words):
    dictionary_words.sort(key=lambda x: (-len(x), x))

    # Checks if a word is found with the letter count
    def can_form(word, letter_count):
        word_count = Counter(word)
        return all(letter_count[char] >= word_count[char] for char in word_count)


    # Backtracks with found words and left over letters
    def backtrack(path, letter_count):
        if sum(letter_count.values()) == 0:
            # If no letters left, we found a valid anagram
            return path

        for word in dictionary_words:
            if can_form(word, letter_count):
                new_letter_count = letter_count - Counter(word)
                result = backtrack(path + [word], new_letter_count)
                if result:
                    return result
        return None

    letter_count = Counter(word)
    
    return backtrack([], letter_count)

def main():
    dictionary_words = []
    words = []
    blank = False

    for line in sys.stdin:
        line = line.rstrip('\n')

        if len(line.strip()) == 0:
            blank = True
            continue

        if not blank:
            words.append(line.lower())
        else:
            dictionary_words.append(line.lower())

    if blank == False:
        print("No Input provided or no seperator")
    else:
        for word in words:
            best_anagram = find_anagrams(word, dictionary_words)
            if best_anagram:
                print(f"{word}: {" ".join(best_anagram)}")
            else:
                print(f"{word}: No anagram found")

if __name__ == "__main__":
    main()

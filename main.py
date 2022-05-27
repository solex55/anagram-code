# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

word = input("enter a word: ")
anagram = input("enter another word: ")

def find_anagram(word, anagram):
    # [assignment] Add your code here

    str1 = word.lower()
    str2 = anagram.lower()

    sorted_str1 = sorted(str1, reverse=True)
    print(sorted_str1)
    sorted_str2 = sorted(str2)

    if sorted_str1 == sorted_str2:
        return True
    else:
        return False

print(find_anagram(word, anagram))


# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    word = input ("Your first word:")
    anagram = input("Your second word:")

    str1 = word
    str2 = anagram

    sort_str1 = sorted(str1)
    sort_str2 = sorted(str2)

    if sort_str1 == sort_str2:     
        return True
    else:      
        return False
    
print (find_anagram('word', 'anagram'))
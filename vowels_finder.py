import random
import string

# Generate a set with random alphabet characters
random_alphabets = set(random.choice(string.ascii_lowercase) for _ in range(100))

def count_vowels(alphabet_set):
    vowels = set("aeiou")
    
    vowel_count = len(alphabet_set.intersection(vowels))
    return vowels, vowel_count

vowels, vowel_count = count_vowels(random_alphabets)

print("Random Alphabets:", random_alphabets)
print("Total vowels:", vowels)
print("Vowel Count:", vowel_count)

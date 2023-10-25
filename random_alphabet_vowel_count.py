import random
import string

# Generate a list with random alphabet characters
random_alphabets = [random.choice(string.ascii_lowercase) for _ in range(100)]

def count_vowels(alphabet_list):
    vowels = "aeiou"

    vowel_counts = {vowel: alphabet_list.count(vowel) for vowel in vowels}
    return vowel_counts,vowels

vowel_counts = count_vowels(random_alphabets)

print("Random Alphabets:", random_alphabets)
print("Vowel Counts:")
for vowel, count in vowel_counts[0].items():
    print(f"{vowel}: {count}")
print("Total vowels:", sum(vowel_counts[0].values()))
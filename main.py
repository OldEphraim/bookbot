def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def count_words(str):
    words = str.split()
    print(len(words))
    return len(words)

def count_letters(str):
    letter_counts = {}

    for char in str:
        char = char.lower()
        if 'a' <= char <= 'z':
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1
    
    print(letter_counts)
    return letter_counts

def generate_report(dict):
    for letter, count in dict.items():
        print(f"The letter {letter} was found {count} times")


frankenstein = main()
count_words(frankenstein)
count_letters(frankenstein)
generate_report(count_letters(frankenstein))
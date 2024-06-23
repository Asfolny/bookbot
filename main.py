def main():
    book = 'books/frankenstein.txt'
    content = get_book_text(book)
    words = word_count(content)
    character_count = letter_count(content)
    character_count.sort(reverse=True, key=lambda d: d["count"])

    # Reporting
    print(f"--- Begin report of {book} ---")
    print(f"{words} words found in the document")
    print()
    
    for char_dict in character_count:
        print(f"The '{char_dict['char']}' character was found {char_dict['count']} times")

    print("--- End report ---")


def get_book_text(path):
    with open(path) as file:
        return file.read()

def word_count(text):
    return len(text.split())

def letter_count(text):
    words = text.split()
    letter_map = {}
    result = []

    for word in words:
        for char in word:
            char = char.lower()
            
            if char.isalpha():
                letter_map[char] = letter_map.get(char, 0) + 1

    for _, (char, count) in enumerate(letter_map.items()):
        result.append({"char": char, "count": count})
    
    return result

main()

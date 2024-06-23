def main():
    book = get_book_text('books/frankenstein.txt')
    words = word_count(book)
    character_count = letter_count(book)
    character_count.sort(reverse=True, key=lambda d: d["count"])
    print(character_count)


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

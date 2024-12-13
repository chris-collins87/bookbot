def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count_words = get_count(text)
    count_characters = character_count(text)
    count_characters.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {book_path} ---")
    print(f"{count_words} words found in the document.")
    print(" ")
    for character in count_characters:
        print(f"The '{character['char']}' character was found {character['num']} times")
    print(" ")
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    lowered_words = text.lower()
    results = {}
    character_dictionary = []
    for letter in lowered_words:
        if letter.isalpha():
            if letter in results:
                results[letter] += 1
            else:
                results[letter] = 1 
    for letter, count in results.items():
        character_dictionary.append({"char": letter, "num": count})
    return character_dictionary

def sort_on(character_count):
    return character_count["num"]
main()

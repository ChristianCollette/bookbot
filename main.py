def main(): 
    book_path = 'books/frankenstein.txt'
    book_text = read_book(book_path)
    print(book_text)
    book_words = book_text.split()
    word_count = len(book_words)
    print(f'{word_count} words found in the document')
    characters = character_count(book_text)
    for character in characters:
        print(f'The \'{character}\' character appears {characters[character]} time(s)')


def read_book(path_to_book):
    with open(path_to_book) as book:
        return book.read()

def character_count(book):
    char_appearances = {}
    formatted_book = book.lower()
    for character in book.lower():
        if character in char_appearances:
            char_appearances[character] += 1
        else:
            char_appearances[character] = 1
    return char_appearances

main()
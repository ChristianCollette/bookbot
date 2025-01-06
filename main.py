def main(): 
    book_path = 'books/frankenstein.txt'
    book_text = read_book(book_path)
    print(book_text)
    book_words = book_text.split()
    word_count = len(book_words)
    print(f'{word_count} words found in the document')
    counted_characters = character_count(book_text)
    sorted_characters = sort_characters(counted_characters)
    for character in sorted_characters:
        print(f'The \'{character['character']}\' character appears {character['count']} time(s)')


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

def sort_method(dict):
    return dict["count"]

def sort_characters(character_counts):
    characters = []
    for character in character_counts:
        characters.append({'character': character, 'count': character_counts[character]})
    characters.sort(reverse=True, key=sort_method)
    return characters
main()
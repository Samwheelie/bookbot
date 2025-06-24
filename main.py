import sys
from stats import word_count, number_repeated_chars, sort_char_dict

def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()
        return content

def main():
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    words = get_book_text(sys.argv[1])
    num_words = word_count(words)
    repeat = number_repeated_chars(words)
    sorted = sort_char_dict(repeat)

    print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in sorted:
        print(f"{entry["char"]}: {entry["num"]}")

main()
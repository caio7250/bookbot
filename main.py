from stats import count_number_of_words, get_book_text, count_number_of_each_char, structure_and_sort_dict
import sys 

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    booktext = get_book_text(filepath)
    number_of_words = count_number_of_words(booktext)
    number_of_chars = count_number_of_each_char(booktext)
    sorted_list = structure_and_sort_dict(number_of_chars)

    print(f"""============ BOOKBOT ============
Analyzing book found at {filepath}...
----------- Word Count ----------
Found {number_of_words} total words
--------- Character Count -------""")
    for item in sorted_list:
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

main()
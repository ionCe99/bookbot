import sys
from stats import get_num_words,num_of_chars




def get_book_text(filepath):
    with open(filepath , 'r') as f:
        file_content = f.read()
    return file_content 

def main(): 
    ###################
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    ######################
    print("============ BOOKBOT ============")
    print(f"Analyzing book {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(filepath)} total words")
    print("--------- Character Count -------")
    num_of_chars(filepath)
    print("============= END ===============")

main()
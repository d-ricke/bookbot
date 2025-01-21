PATH_TO_FILE = "books/frankenstein.txt"

def main(book_path = PATH_TO_FILE):
    text = get_book_text(book_path)
    #print(text)
    #print(f"The document contains {get_num_words(text)} words")
    #print(get_char_counts(text))
    print_char_counts_report(get_char_counts_report_list(get_char_counts(text)))

def get_num_words(text):
    return len(text.split())   

def sort_on(dict):
    return dict["ct"] 

def get_char_counts(text):
    lowered_text = text.lower()
    char_counts = {}
    for char in lowered_text:
        if char in char_counts.keys():
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return (char_counts)

def get_char_counts_report_list(counts):
    new_counts = []
    for count_key in counts:
        if count_key.isalpha():
            new_counts.append({'key':count_key, 'ct':counts[count_key]})
    new_counts.sort(key=sort_on, reverse=True)
    return(new_counts)

def print_char_counts_report(counts_report):
    for bb in counts_report:
        print(f"The '{bb['key']}' character was found {bb['ct']} times")

def get_book_text(path):
    with open(PATH_TO_FILE) as f:
        return f.read()
    


main()
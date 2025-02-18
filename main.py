def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    character_counts = {}
    
    text_lowercase = text.lower()

    for c in text_lowercase:
        if c in character_counts:
            character_counts[c] += 1
        else:
            character_counts[c] = 1
    return character_counts

def print_report():
    with open("books/frankenstein.txt") as f:
        text = f.read()
    
    counts_dict = count_characters(text)
    word_count = count_words(text)

    list_counts_dict = []

    for k in counts_dict:
        dict_item = {}
        if k.isalpha():
            dict_item["char"] = k
            dict_item["count"] = counts_dict[k]
            list_counts_dict.append(dict_item)
    list_counts_dict.sort(reverse=True,key=sort_on_count)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    for dict_item in list_counts_dict:
        print(f"The '{dict_item["char"]}' character was found {dict_item["count"]} times")
    print("--- End report ---")
    
def sort_on_count(dict):
    return dict["count"]

def main():
    print_report()
    
main()

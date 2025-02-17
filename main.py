def count_words(text):
    words = text.split()
    return len(words)







def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(count_words(file_contents))


main()

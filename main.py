def main():
    #print(file_contents)
    print(word_count(file_contents))


def word_count(text):
    words = text.split()
    return len(words)

with open("books/frankenstein.txt") as f:
    file_contents = f.read()


main()
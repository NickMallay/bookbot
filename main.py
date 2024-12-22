def main():
    print("--- Begin report of books/frankenstein.txt ---")
    final_word_count = word_count(file_contents)
    print(str(final_word_count) + " words found in the document")
    character_dict = count_characters(file_contents)
    ordered_list = order_characters(character_dict)
    display_list(ordered_list)

def display_list(ordered_list):
        for d in ordered_list:
            print(f"The '{d["character"]}' character was found {d["count"]} times")



def sort(dict):
    return dict["count"]

def order_characters(characters):
    character_list = []
    for c in characters:
        character_list.append({"character": c, "count": characters[c]})
    character_list.sort(key=sort, reverse=True)
    return character_list


def count_characters(text):
    #define dictionary to hold characters and their count
    character_dict = {}
    #make input all lower case so upper and lower case letters are not counted seperately
    lower_text = text.lower()
    for character in lower_text:
        if character.isalpha():
            if not character in character_dict:
                character_dict[character] = 0
            character_dict[character] += 1
    return character_dict

def word_count(text):
    words = text.strip().split()
    return len(words)

with open("books/frankenstein.txt") as f:
    file_contents = f.read()


main()
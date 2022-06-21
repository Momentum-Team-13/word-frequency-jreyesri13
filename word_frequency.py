import re

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


# Read in file and print out the frequency of words in that file.
def print_word_freq(file):
    step1 = read_the_file(file)
    step2 = remove_punctuation(step1)
    step3 = split_input(step2)
    step4 = lowercase_values(step3)
    step5 = remove_stop_words(step4)
    step6 = word_counter(step5)
    step7 = sort_dict(step6)

    for keyz, valuez in step7.items():
        formatted = f"{keyz} | {valuez}" + " *" * valuez
        print(formatted)


# Function to read text from the file.
def read_the_file(var1):
    with open(var1) as open_file:
        read_file = open_file.read()

    return read_file


# Function to remove all the punctuation.
def remove_punctuation(var1):
    var2 = re.sub(r'[^\w\s]', '', var1)
    return var2


# Function to split strings into a list.
def split_input(var1):
    var2 = var1.split()
    return var2


# Function to apply lowercase to all words.
def lowercase_values(var1):
    list2 = []
    for i in var1:
        list2.append(i.lower())

    return list2


# Function to remove stop words.
def remove_stop_words(var1):
    var1_copy = var1.copy()
    for i in var1_copy:
        if i in STOP_WORDS:
            var1.remove(i)

    return var1


# Function that counts words and creates a dictionary.
def word_counter(var1):
    word_count = {}

    for word in var1:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


# Sort the dictionary by the values in descending order.
def sort_dict(var1):
    sorted_items = sorted(var1.items(), key=lambda item: item[1], reverse=True)
    # sorted_dict = dict(sorted_items)
    ten_items = sorted_items[:10]
    ten_dict = dict(ten_items)

    return ten_dict


# Testing out the program.
# print_word_freq("praise_song_for_the_day.txt")
# print_word_freq("the-hill-we-climb.txt")


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)

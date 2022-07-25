# offline

import re
import os
import shutil

USER_PATH_ZIP = r"C:\Users\nechama\Desktop\bootcamp\google\arc.zip"
USER_PATH = r"C:\Users\nechama\Desktop\bootcamp\google\arc"


def enter_to_dictionary(sentence: str, line_number: int, path: str, word_dictionary: dict) -> None:
    """
    The function add the words and their locations on the sentence to the dictionary
    :param sentence:
    :param line_number: The sentence's line number on the text.
    :param path:
    :param word_dictionary:
    :return:
    """
    words = [word.lower() for word in re.findall(r'\w+', sentence)]
    for word in words:
        if word in word_dictionary:
            word_dictionary[word].add(tuple((path, line_number)))
        else:
            word_dictionary[word] = {tuple((path, line_number))}


def read_file(path: str, word_dictionary: dict) -> None:
    with open(path,encoding="utf8") as file:
        number_line = 0
        for sentence in file:
            number_line += 1
            enter_to_dictionary(sentence, number_line, path, word_dictionary)


def pass_all_files(root_path: str,words_dictionary:dict) -> None:
    # shutil.unpack_archive(USER_PATH_ZIP, USER_PATH)  # extract the zip file need to execute only in the first time
    for file in os.listdir(root_path):
        if file.endswith('.txt'):
            read_file(root_path + '\\' + file, words_dictionary)
        else:
            pass_all_files(root_path + '\\' + file)


def main():
    words_dictionary = dict()
    pass_all_files(USER_PATH,words_dictionary)
    print(words_dictionary)


if __name__ == "__main__":
    main()





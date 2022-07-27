# offline

import re
import os
import shutil

import pygtrie

USER_PATH_ZIP = r"C:\Users\nechama\Desktop\bootcamp\google\arc.zip"
USER_PATH = r"C:\Users\97252\bootcamp\projects\google\Archive"


def enter_to_dictionary(sentence: str, line_number: int, path: str, word_dictionary: pygtrie.CharTrie) -> None:
    """
    The function add the words and their locations on the sentence to the dictionary
    :param sentence:
    :param line_number: The sentence's line number on the text.
    :param path:
    :param word_dictionary:
    """
    words = [word.lower() for word in re.findall(r'\w+', sentence)]
    for word in words:
        if word in word_dictionary:
            word_dictionary[word].add(tuple((path, line_number)))
        else:
            word_dictionary[word] = {tuple((path, line_number))}


def read_file(path: str, word_dictionary: pygtrie.CharTrie) -> None:
    """
    Get path of file and open it and add to the trie tree all the words that exist in this file.
    :param path: The path of the file we want to read from.
    :param word_dictionary: The data struct for saving the words and their locations.
    """
    with open(path, encoding="utf8") as file:
        number_line = 0
        for sentence in file:
            number_line += 1
            enter_to_dictionary(sentence, number_line, path, word_dictionary)


def pass_all_files(root_path: str, words_dictionary: pygtrie.CharTrie) -> None:
    """
    The function gets the root path and pass all over the files and directory recursively.
    :param root_path: The path of the root, the main directory to work on.
    :param words_dictionary: The data struct to work with and to add the data to.
    """
    # shutil.unpack_archive(USER_PATH_ZIP, USER_PATH)  # Extract the zip file. Need to execute only in the first time.
    for file in os.listdir(root_path):
        if file.endswith('.txt'):
            read_file(root_path + '\\' + file, words_dictionary)
        else:
            pass_all_files(root_path + '\\' + file, words_dictionary)


def main():
    words_trie = pygtrie.CharTrie()
    pass_all_files(USER_PATH, words_trie)
    return words_trie


if __name__ == "__main__":
    main()




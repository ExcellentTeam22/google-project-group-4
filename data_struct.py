import re
import os
import shutil

USER_PATH_ZIP = r"C:\Users\nechama\Desktop\bootcamp\google\arc.zip"
USER_PATH = r"C:\Users\nechama\Desktop\bootcamp\google\arc"


def enter_to_dictionary(sentence: str, line_number: int, path: str, word_dictionary: dict):
    words = [word.lower() for word in re.findall(r'\w+', sentence)]
    for word in words:
        if word in word_dictionary:
            word_dictionary[word].add(tuple((path, line_number)))
        else:
            word_dictionary[word] = {tuple((path, line_number))}

# d = dict()
# enter_to_dictionary("hello, I am student student!", 1, "c:/", d)
# enter_to_dictionary("hello,good morning I am happy!", 2, "c:/", d)
# print(d)

def read_file(path: str, word_dictionary: dict):
    with open(path,encoding="utf8") as file:
        number_line = 0
        for sentence in file:
            number_line += 1
            enter_to_dictionary(sentence, number_line, path, word_dictionary)

d = dict()

def pass_all_files(root_path: str):
    #shutil.unpack_archive(USER_PATH_ZIP, USER_PATH)
    for file in os.listdir(root_path):
        if file.endswith('.txt'):
            read_file(root_path + '\\' + file, d)
        else:
            pass_all_files(root_path + '\\' + file)


#main:

# offline
pass_all_files(USER_PATH)
print(d)

# online
user_text = "hello my name"


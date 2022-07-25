# online
import re
import data_struct
import linecache

WORD_DICTIONARY = data_struct.main()


def clear_sentence(sentence: str):
    return ' '.join(re.findall(r'\w+', sentence))


def find_includes_sentences(sentences:set,sub_sentence:str):
    return [sentence for sentence in sentences if sub_sentence in clear_sentence(sentence)]



def from_offset_to_sentence(locations: set):
    sentences = [linecache.getline(location[0], location[1]) for location in locations]

    print(sentences)
    return sentences


def user_query():
    sentence = input("Hello, enter the text that you to find:\n")
    words = re.findall(r'\w+', sentence.lower())

    # check if the first word is exist
    locations_intersections = set(WORD_DICTIONARY[words[0]])

    for index,word in enumerate(words):
        if index != 0 and word in WORD_DICTIONARY:
            locations_intersections = locations_intersections.intersection(WORD_DICTIONARY[word])
        if not word in WORD_DICTIONARY:
            locations_intersections = {}
            break
    print(find_includes_sentences(from_offset_to_sentence(locations_intersections),' '.join(words)))




def main():
    user_query()


if __name__ == "__main__":
    main()
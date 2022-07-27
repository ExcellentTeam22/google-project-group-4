# online
import re
import data_struct
import linecache
import AutoCompleteData

WORD_TRIE = data_struct.main()

RESULTS_NUMBER = 5


def clear_sentence(sentence: str):
    return ' '.join(re.findall(r'\w+', sentence))


def scoring(sub_sentence):
    return len(sub_sentence)*2


def from_location_to_autocomplete(location , sub_sentence):
    sentence = linecache.getline(location[0], location[1])
    if sub_sentence in clear_sentence(sentence):
        return AutoCompleteData.AutoCompleteData(sentence,location[0].split('\\')[-1][:-4:],location[1],scoring(sub_sentence))
    return None


def fix_sentence():
    return set()


def sorting(auto_complete_candidates):
    return list(auto_complete_candidates)[:5]


def user_query():
    sentence = input("Hello, enter the text that you to find:\n")
    words = re.findall(r'\w+', sentence.lower())


    # check if the first word is exist
    locations_intersections = set(WORD_TRIE[words[0]])

    for index,word in enumerate(words):
        if index != 0 and word in WORD_TRIE:
            locations_intersections = locations_intersections.intersection(WORD_TRIE[word])
        if word not in WORD_TRIE:
            locations_intersections = {}
            break

    auto_complete_candidates = {from_location_to_autocomplete(location,' '.join(words)) for location in locations_intersections} - {None}
    if len(auto_complete_candidates ) < RESULTS_NUMBER:
        auto_complete_candidates=auto_complete_candidates.union(fix_sentence())

    top_five = sorting(auto_complete_candidates)

    [print(i) for i in auto_complete_candidates]


def main():
    user_query()


if __name__ == "__main__":
    main()


def get_location_by_prefix(prefix: str):
    """
    The function get a prefix and return the locations of the words that start with this prefix
    """
    item_iterator = iter(WORD_TRIE.items(prefix=prefix))
    if prefix in WORD_TRIE:
        next(item_iterator)
    for item in item_iterator:
        yield item[1]


def prefix_locations_intersection(prefix: str, words):
    """
    The function get a prefix and return the intersection of the prefix's locations with the locations of the other words
    """

    for locations in get_location_by_prefix(prefix):
        yield set.intersection(*[locations]+[WORD_TRIE[word] for word in words[:-2]])


def intersections_without_word(words, without_word):
    """
    The function returns the intersection of the locations of the words without one word
    """
    locations = {WORD_TRIE.get(word) for word in words if word != without_word}
    if None in locations:
        return {}
    return set.intersection(*locations)



def is_change_one_char(word: str):
    for index, char in reversed(list(enumerate(word[-1::-1]))):
        for i in range(97, 123):
            if chr(i) != word[index] and word[0:index] + chr(i) + word[index+1:] in WORD_TRIE:
                yield word[0:index] + chr(i) + word[index+1:]
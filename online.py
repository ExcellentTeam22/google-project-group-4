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


def find_word_in_trie(word_fix: str) -> set:
    return set(WORD_TRIE[word_fix])


def add_letter(word: str) -> str:
    size_of_word = len(word)
    word = word[::-1]  # reverse
    for index_letter in range(size_of_word + 1):
        for j in range(97, 123):  # move from a to z
            word_fix = word[:index_letter] + chr(j) + word[index_letter:]
            word_fix = word_fix[::-1]  # reverse
            # print(new_word)
            if word_fix in online.WORD_TRIE:
                yield word_fix


def remove_letter(word: str) -> str:
    size_of_word = len(word)
    word = word[::-1]  # reverse
    for index_letter in range(size_of_word):
        word_fix = word[:index_letter] + word[index_letter+1:]
        word_fix = word_fix[::-1]  # reverse
        # print(new_word)
        if word_fix in online.WORD_TRIE:
            yield word_fix


def fix_word_add_remove(word_to_fix: str):
    # Insert letter:
    while True:
        word_fix = add_letter(word_to_fix)
        locations_of_word = find_word_in_trie(word_fix)
        if locations_of_word:
            yield locations_of_word

    # Remove letter:
    while True:
        word_fix = remove_letter(word_to_fix)
        locations_of_word = find_word_in_trie(word_fix)
        if locations_of_word:
            yield locations_of_word






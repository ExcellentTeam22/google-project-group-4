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
    for locations in  WORD_TRIE.items(prefix=prefix):
        yield locations[1]
    #prefix_locations = set.union(*(locations[1] for locations in WORD_TRIE.items(prefix=prefix))) #{WORD_TRIE.items(prefix=prefix)}
   # return prefix_locations


def get_sentences_by_prefix(prefix:str,words):
    for locations in get_location_by_prefix(prefix):
        yield set.intersection(*[locations]+[WORD_TRIE[word] for word in words[:-2]])

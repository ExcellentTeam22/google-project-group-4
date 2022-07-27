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


def location_to_autocomplete(location , sub_sentence):
    sentence = linecache.getline(location[0], location[1])
    if sub_sentence in clear_sentence(sentence):
        return AutoCompleteData.AutoCompleteData(sentence,location[0].split('\\')[-1][:-4:],location[1],scoring(sub_sentence))
    return None


def get_location_by_prefix(prefix: str):
    """
    The function get a prefix and return the locations of the words that start with this prefix
    """
    if WORD_TRIE.has_subtrie(prefix):
        item_iterator = iter(WORD_TRIE.items(prefix=prefix))
        if prefix in WORD_TRIE:
            next(item_iterator)
        for item in item_iterator:
            yield item[0],item[1]


def intersections_without_word(words: list, without_word: str):
    """
    The function returns the intersection of the locations of the words without one word
    """

    locations = [WORD_TRIE.get(word) for word in words if word != without_word]
    if None in locations or not locations:
        return set()
    print(locations)
    return set.intersection(*locations)


def sorting(auto_complete_candidates):
    return list(auto_complete_candidates)[:5]


def is_change_one_char(word: str):
    for index, char in reversed(list(enumerate(word[-1::-1]))):
        for i in range(97, 123):
            if chr(i) != word[index] and word[0:index] + chr(i) + word[index+1:] in WORD_TRIE:
                fix_word = word[0:index] + chr(i) + word[index+1:]
                yield fix_word,find_word_in_trie(fix_word)






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
            if word_fix in WORD_TRIE:
                yield word_fix


def remove_letter(word: str) -> str:
    size_of_word = len(word)
    word = word[::-1]  # reverse
    for index_letter in range(size_of_word):
        word_fix = word[:index_letter] + word[index_letter+1:]
        word_fix = word_fix[::-1]  # reverse
        # print(new_word)
        if word_fix in WORD_TRIE:
            yield word_fix


def fix_word_add_remove(word_to_fix: str) -> set:

    # Insert letter:
    for word_fix in add_letter(word_to_fix):
        yield word_fix,find_word_in_trie(word_fix)

    # Remove letter:
    for word_fix in remove_letter(word_to_fix):
        yield word_fix,find_word_in_trie(word_fix)







def fix_sentence(words: list,number_of_result:int):
    results = set()
    locations = intersections_without_word(words,words[-1])
    sub_sentence = " ".join(words)
    for fix_word,prefix_locations in get_location_by_prefix(words[-1]):
        if len(words) <= 1:
            intersection_locations = prefix_locations
        else:
            intersection_locations = locations.intersection(prefix_locations)
        results = results.union({location_to_autocomplete(location," ".join(words[:-2]+[fix_word])) for location in intersection_locations} -{None} )
        if len(results) >= number_of_result:
            return results

    for word in words[-1::-1]:
        locations = intersections_without_word(words, word)
        for fix_word,fix_location in  is_change_one_char(word):
            if len(words)<=1:
                intersection_locations=fix_location
            else:
                intersection_locations = locations.intersection(fix_location)
            results=results.union({location_to_autocomplete(location,sub_sentence.replace(word,fix_word)) for location in intersection_locations} - {None})
            if len(results) >= number_of_result:
                return results

    for word in words[-1::-1]:
        locations = intersections_without_word(words, word)
        for fix_word,fix_location in  fix_word_add_remove(word):
            if len(words) <= 1:
                intersection_locations = fix_location
            else:
                intersection_locations = locations.intersection(fix_location)
            results=results.union({location_to_autocomplete(location,sub_sentence.replace(word,fix_word)) for location in intersection_locations} - {None})
            if len(results) >= number_of_result:
                return results


def user_query():
    sentence = input("Hello, enter the text that you to find:\n")
    words = re.findall(r'\w+', sentence.lower())


    # check if the first word is exist
    locations_intersections = intersections_without_word(words,None)

    auto_complete_candidates = list({location_to_autocomplete(location,' '.join(words)) for location in locations_intersections} - {None})
    #print("the candidate: ", auto_complete_candidates)

    if auto_complete_candidates or len(auto_complete_candidates ) < RESULTS_NUMBER:
        auto_complete_candidates+=list(fix_sentence(words,RESULTS_NUMBER-len(auto_complete_candidates )))

    top_five = auto_complete_candidates[:5] #need to sort

    [print(i) for i in top_five]


def main():

    user_query()


if __name__ == "__main__":
    main()



#
#
# def prefix_locations_intersection(prefix: str, words):
#     """
#     The function get a prefix and return the intersection of the prefix's locations with the locations of the other words
#     """
#
#     for locations in get_location_by_prefix(prefix):
#         yield set.intersection(*[locations]+[WORD_TRIE[word] for word in words[:-2]])


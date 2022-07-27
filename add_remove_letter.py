import online


def find_word_in_trie(word_fix: str) -> set:
     return set(online.WORD_TRIE[word_fix])


def add_letter(word: str) -> set:
    size_of_word = len(word)
    word = word[::-1]  # reverse
    for index_letter in range(size_of_word + 1):
        for j in range(97, 123):  # move from a to z
            word_fix = word[:index_letter] + chr(j) + word[index_letter:]
            word_fix = word_fix[::-1]  # reverse
            # print(new_word)
            locations_of_word = find_word_in_trie(word_fix)
            if locations_of_word:
                yield locations_of_word


def remove_letter(word: str) -> set:
    size_of_word = len(word)
    word = word[::-1]  # reverse
    for index_letter in range(size_of_word):
        word_fix = word[:index_letter] + word[index_letter+1:]
        word_fix = word_fix[::-1]  # reverse
        # print(new_word)
        locations_of_word = find_word_in_trie(word_fix)
        if locations_of_word:
            yield locations_of_word


remove_letter('hi')
add_letter('hi')

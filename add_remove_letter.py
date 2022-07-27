import online


def find_word_in_trie(word_fix: str) -> set:
     return set(online.WORD_TRIE[word_fix])


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


fix_word_add_remove("hi")
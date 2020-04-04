"""
Zachary Keeffe
"""
def __main__():
    word_to_count = {}
    text = input("Text: ")
    words = text.split()
    for word in words:
        frequency = word_to_count.get(word, 0)
        word_to_count[word] = frequency + 1

    # Print the unique words and their frequencies in alphabetical order
    words = list(word_to_count.keys())
    words.sort()

    # use the max function to find the maximum of the values produced by the
    # generator function (like a list comprehension) of lengths of words
    max_length = max((len(word) for word in words))
    for word in words:
        print("{:{}} : {}".format(word, max_length, word_to_count[word]))


__main__()

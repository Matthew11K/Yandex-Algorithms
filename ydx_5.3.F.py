def shorten_words(dictionary, text):
    sorted_dict = sorted(set(dictionary), key=len)

    text_words = text.split()

    for i, word in enumerate(text_words):
        for dict_word in sorted_dict:
            if word.startswith(dict_word):
                text_words[i] = dict_word
                break

    return ' '.join(text_words)

dictionary = input().split()
text = input()
print(shorten_words(dictionary, text))

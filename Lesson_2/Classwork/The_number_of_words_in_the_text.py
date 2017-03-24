def funct(text, count_of_words_in_text):
    text = text.lower()
    real_words_count = 0
    for word in count_of_words_in_text:
        if word in text:
            real_words_count += 1

    return real_words_count


words = set(["how", "are", "you", "hello"])
print(funct("How aresjfhdskfhskd you?", words))
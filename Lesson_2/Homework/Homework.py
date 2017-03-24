def find_message(text):
    letters_box = ''
    for letter in text:
        if letter.isupper():
            letters_box += letter
    return letters_box

print find_message("How are you? Eh, ok. Low or Lower? Ohhh.")


def only_upper(text):
    return filter(lambda letter: letter.isupper(), text)

print only_upper("HeLLo WorLD")


def only_upper(text):
    return "".join(letter for letter in text if letter.isupper())

print only_upper("HeLLo WorLD")

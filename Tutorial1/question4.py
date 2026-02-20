def num_vowels(text):
    vowels  = "a e i o u"
    num_vowels = 0
    text = text.lower()
    for i in range(len(text)):
        if text[i] in vowels:
            num_vowels += 1
    return num_vowels
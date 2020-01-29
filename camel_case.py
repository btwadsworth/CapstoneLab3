def camel_case(sentence):

    # convert sentence into camel case and return
    words = sentence.split(' ')
    new_sentence = ''
    first_word_done = False
    for word in words:
        if not first_word_done:
            camel = word.lower()
            first_word_done = True
        else:
            camel = word.capitalize()
        new_sentence += camel
    return new_sentence

def main():
    sentence = input('Enter your sentence: ')
    camelCased = camel_case(sentence)
    print(camelCased)

if __name__ == '__main__':
    main()

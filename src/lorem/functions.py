from random import randint

from src.lorem.consts import LOREM_PARAGRAPHS, LOREM_WORDS, LOREM_VOWELS


def get_random(lorem_list):
    index = randint(0, len(lorem_list) - 1)

    return lorem_list[index]


def get_paragraph():
    return get_random(LOREM_PARAGRAPHS)


def get_sentences():
    return [
        sentence + '.'
    for sentence in get_paragraph().split('. ')]


def get_sentence():
    return get_random(get_sentences())


def get_words():
    return LOREM_WORDS


def get_word():
    return get_random(get_words())


def get_lorem(name, *args, **kwargs):
    return {
        'paragraph': get_paragraph,
        'sentence': get_sentence,
        'words': get_words,
        'word': get_word,
    }[name](*args, **kwargs)


def generate_syllable():
    word = get_word()
    word = word[randint(0, len(word) - 3):] if len(word) > 2 else word
    syllable = word[0]

    for letter in word:
        if letter == syllable:
            continue

        syllable += letter

        if not letter in LOREM_VOWELS:
            break
    
    return syllable


def generate_word():
    word = ''
    syllables = [
        generate_syllable()
    for _ in range(randint(1, 4))]

    for i in range(len(syllables)):
        syllable = syllables[i]

        if (i < len(syllables) - 1) and (syllables[i + 1][0] not in LOREM_VOWELS):
            word += syllable[:-1]
        else:
            word += syllable

    return word


def generate_words(words_count = 10):
    return ' '.join([
        generate_word() 
    for _ in range(words_count)])


def generate_sentence(words_count = 25):
    sentence = generate_words(words_count)
    
    return sentence.capitalize() + '.'


def generate_paragraph(sentences_count = 4, words_count = 25):
    return ' '.join([
        generate_sentence(words_count - 10 + randint(0, 10)) 
    for _ in range(sentences_count)])


def generate_lorem(name, *args, **kwargs):
    return {
        'paragraph': generate_paragraph,
        'sentence': generate_sentence,
        'words': generate_words,
        'word': generate_word,
    }[name](*args, **kwargs)
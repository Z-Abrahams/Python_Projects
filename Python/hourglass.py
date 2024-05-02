""" A recursive function that receives a word as input and prints it out in the form of an hourglass."""


def hglass(word):
    if len(word) == word.count(' '):
        return
    else:
        print(word[::-1] + word)
        hglass(word[1:] + ' ')
        print(word[::-1] + word)

hglass(input('Enter a word:\n'))

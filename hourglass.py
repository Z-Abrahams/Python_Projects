""" A function that receives a word as input and prints it out in the form of an hourglass."""


def hglass(word, word_lst=[]):
    if len(word) == word.count(' '):
        del word_lst[len(word_lst)-1]

        for i in reversed(word_lst):
            print(i[::-1] + i)
        
        return
    else:
        print(word[::-1] + word)
        word_lst.append(word)
        num_spaces = word.count(' ')

        if num_spaces != 0:
            word = word.strip()
            word = word[1:]
            for i in range(num_spaces+1):
                word = word + ' '

            return hglass(word, word_lst)
        else:
            word = word[1:] + ' '
            return hglass(word, word_lst)

hglass(input('Enter a word:\n'))

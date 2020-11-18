def punc_removal(bag_of_words):
    '''
    :param bag_of_words: str;
    :return: str with all punctuation removed
    Also removes 4, 3, and 2 blank spaces
    '''
    punc = "#$!%^&*()@-=_+]/[}{\|;':,./<>?`~\""
    for symbol in punc:
        bag_of_words = bag_of_words.replace(symbol, '').replace('    ', ' ').replace('   ', ' ').replace('  ', ' ')
    return bag_of_words


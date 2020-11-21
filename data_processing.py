def punc_removal(bag_of_words):
    '''
    :param bag_of_words: str;
    :return: str with all punctuation removed
    Also removes 4, 3, and 2 blank spaces
    '''
    punc = "#$!%^&*()@-=_+]/[}{\|;':,./<>?`~\""
    for symbol in punc:
        bag_of_words = bag_of_words.replace(symbol, '').replace('    ', ' ')\
                       .replace('   ', ' ').replace('  ', ' ')
    return bag_of_words

def scaler(series, top_range, bottom_range):
    '''
    Scales data between a range between (bottom_range, top_range
    Current values are hard coded as max(x) = 92 and min(x) = 1,
    due to the current Elite Meet member numbers
    '''
    multiplier = top_range - bottom_range
    numerator = series - 1
    #denominator = max(series) - min(series)
    denominator = 91
    ans = multiplier * numerator/denominator
    return ans + bottom_range


if __name__ == '__main__':

    import pandas as pd

    df = pd.read_csv('vets_coords.csv')
    nums = df['Combined']
    print(scaler(nums, 22, 4))
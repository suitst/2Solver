# Solves the NYTimes Letterboxed Game in Two Words
# Tim Suits (2023)

import pandas as pd
from time import time


def get_sides():
    d = {}
    north = input("Enter the top three letters: ")
    if len(north) != 3:
        raise Exception("Each side must have only three letters")
    else:
        for letter in list(north):
            d[letter] = 'north'
        east = input("Enter the right three letters: ")
        if len(east) != 3:
            raise Exception("Each side must have only three letters")
        else:
            for letter in list(east):
                d[letter] = 'east'
            south = input("Enter the bottom three letters: ")
            if len(south) != 3:
                raise Exception("Each side must have only three letters")
            else:
                for letter in list(south):
                    d[letter] = 'south'
                west = input("Enter the left three letters: ")
                if len(north) != 3:
                    raise Exception("Each side must have only three letters")
                else:
                    for letter in list(west):
                        d[letter] = 'west'
                    return d


def is_valid(word, sides):
    letters = list(str(word))
    return set(letters).issubset(set(sides.keys()))


def is_different_sides(word, sides):
    letters = list(str(word))
    current_side = ''
    for letter in letters:
        if sides[letter] != current_side:
            current_side = sides[letter]
        else:
            return False
    return True


def filter_words(words, sides):
    filtered = []
    for word in words:
        if is_valid(word, sides):
            if is_different_sides(word, sides):
                filtered.append(word)
    return filtered


def is_solved(word1, word2, sides):
    required_letters = sides.keys()
    proposed_letters = []
    for word in [word1, word2]:
        for letter in list(str(word)):
            proposed_letters.append(letter)
    return set(required_letters).issubset(set(proposed_letters))


def find_pairs(words, sides):
    pairs = []
    connected = 0
    for word1 in words:
        for word2 in words:
            if list(str(word2))[0] == list(str(word1)).pop():
                connected += 1
                if is_solved(word1, word2, sides):
                    pairs.append((word1, word2))
    print(f'Found {connected:,} connected pairs.')
    print(f'There are {len(pairs)} possible 2solves.')
    if len(pairs) > 0:
        print(f'2solves: {pairs}')


def main():
    print('\n')
    print('2Solver!')
    print('\n')
    print('Loading dictionary...')
    words_df = pd.read_csv('./words_proc.csv')
    word_list = words_df["Words"].values.tolist()
    print('Dictionary loaded.')
    game_sides = get_sides()
    print('Processing...')
    start = time()
    filtered_words = filter_words(word_list, game_sides)
    print(f'Found {len(filtered_words):,} suitable words.')
    find_pairs(filtered_words, game_sides)
    stop = time()
    runtime = stop - start
    print(f'Processing time: {round(runtime, 1)} s.')


if __name__ == "__main__":
    main()

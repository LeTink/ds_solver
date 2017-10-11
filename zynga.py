#!/usr/bin/python
import sys
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="unscramble Drawsomething words")
    parser.add_argument("n", type=int, help="number of characters")
    parser.add_argument("s", type=str, help="available letters")
    parser.add_argument("-d", action="store_true", help="also check standard dict")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-en", action="store_true", help="English words")
    group.add_argument("-es", action="store_true", help="Spanish words")
    group.add_argument("-de", action="store_true", help="German words")
    return parser.parse_args()

def find_word(words, n, s):
    # set-up a flag to see if we need to trawl through 'proper' dictionaries as
    # well as the ds_wor-lists
    gotcha = False
    for word in words:
        if len(word) == n:
            garble = list(s.lower())
            for letter in word.lower():
                if letter not in garble: 
                    break
                # if the current letter from word is in the list of
                # letters, append it to tally and pop it out of the list of
                # original letters (we don't want false positives for
                # multiple identical letters if they're not really present)
                garble.pop(garble.index(letter))
            else: 
                print word
                gotcha = True
    return gotcha



def main():
    # set the language to default to English
    lang = 'en'
    args = parse_args()

    # check whether Spanish or German were requested
    if args.es:
        lang='es'
    if args.de:
        lang='de'
    s = args.s
    n = args.n
      
    # read all words in dictionary into a list
    with open('ds_words.'+lang) as f:
      words = list(f.read().splitlines())
    print( "From Drawesomething wordlist:" )
    gotcha = find_word( words, n, s)


    if gotcha == False or args.d:
        print( "From standard american dictionary:" )
        with open(lang) as f:
            words = list(f.read().splitlines())
        find_word(words, n, s)

if __name__ == "__main__":
    main()

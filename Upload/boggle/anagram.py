"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

d = {}


def main():
    print('Welcome to stanCode "Anagram Generator"! ')
    target = input('Find anagrams for (or -1 to quit) :  ')
    while True:
        if target == EXIT:
            print('See you next time!')
            break
        else:
            read_dictionary()
            find_anagrams(target)
            target = input('Find anagrams for (or -1 to quit) :  ')


def read_dictionary():
    global d
    with open(FILE, 'r') as f:
        for line in f:
            word = line.strip('\n')
            d[word]=word


def find_anagrams(s):
    """
    :param s: the string input by user
    :return: different permutations of string's alphabet in the dictionary
    """
    result = []
    count = []
    find_anagrams_helper(s, '', result, count, [])
    print(int(len(count)), ' anagrams :', result)


def find_anagrams_helper(s, current, result, count, location):
    """
    :param s: the string input by user
    :param current: a blank string to store letters
    :param result: a list to store the word found in the dictionary
    :param count: a list to store the number of words
    :param location: a list to store the index of alphabet
    :return: the permutations of string's alphabet can be found in the dictionary
    """

    global d
    if len(current) == len(s) and current not in result and current in d:
        print('Searching...')
        print('Found : ' + current)
        result.append(current)
        count.append(1)
    else:
        for i in range(len(s)):
            ele = s[i]
            # tutors help me use the concept of index to solve the problem of same alphabet in a word
            if i not in location:
                location.append(i)
                if has_prefix(current):  # this function won't practically make the process faster.
                    find_anagrams_helper(s, current + ele, result, count, location)
                location.pop()


def has_prefix(sub_s):
    """
    :param sub_s: the list which includes the permutations of string's alphabet
    :return: if the permutations of string's alphabet not exists in dictionary
    """
    global d
    for word in d:
        if d[word].startswith(sub_s):
            return True
    return False




if __name__ == '__main__':
    main()

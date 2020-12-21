"""
File: boggle.py
Name: Elsa
----------------------------------------
This file shows the game boggle that player can find words
that constructed by neighboring letters on a 4x4 square grid.
The length of the word should be at least 4 letters and a letter only been reviewed once.
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

d = {}


def main():
    """
    This program shows the possible words which has at least 4 alphabets on a 4x4 square grid.
    """
    initial = ''
    # to make sure the input format is correct
    # to get a string by input
    for i in range(4):
        row = input(str(i + 1) + ' row of letters :')
        if input_correct(row) is False:
            break
        for ch in row:
            ch.lower()
            if ch is not ' ':
                initial += ch

    # a list created to get the gradation of string
    board = [[*initial[0:4]], [*initial[4:8]], [*initial[8:12]], [*initial[12:16]]]
    read_dictionary()
    find_permutations(board)


def find_permutations(board):
    """
    :param board: a nested list of string input by players
    :return: the final result in dictionary
    """
    global d
    count = 0
    final_result = []

    # to get the result from the function with nested list and move the element into a new list
    for row in range(4):
        for column in range(4):
            for word in find_permutations_helper(board, row, column, '', []):
                if not word in final_result:
                    final_result.append(word)

    # to check if the word exist in dictionary
    for word in final_result:
        if word in d:
            count += 1
            print('Found :', word)
    print('There are ', count, ' words in total.')


def find_permutations_helper(board, row, column, current, list_words):
    """
    :param board: a nested list of string input by players
    :param row: the first level of the nested list
    :param column:the second level of the nested list
    :param current: a string to store the new string
    :param list_words: a list to store possible words
    :return: all possible words from a given starting position [row, column]
    """
    if len(current) > 4:
        return
    if row in (4, -1) or column in (4, -1):
        return

    # using the situation of position to create a new string
    if board[row][column] != " ":
        if has_prefix(current + board[row][column]):

            # create a new board with the elements in initial board
            new_board = [[*board[0:4][0]], [*board[0:4][1]], [*board[0:4][2]], [*board[0:4][3]]]

            # change the situation of position in new board to make sure an alphabet only been reviewed once
            new_board[row][column] = " "

            # explore next position around the letter
            next_move = [(1, 1), (-1, -1), (1, -1), (-1, 1), (1, 0), (0, 1), (-1, 0), (0, -1), ]
            for x, y in next_move:
                find_permutations_helper(new_board, row + x, column + y, current + board[row][column], list_words)

            # add a new word to list
            if len(current + board[row][column]) >= 4:
                list_words.append(current + board[row][column])

            return list_words


def input_correct(s):
    """
    :param s:the string that player input
    :return: if the input format is correct
     """

    for i in range(len(s)):
        ch = s[i]
        if i % 2 != 0 and ch != ' ':
            print('Illegal input')
            return False
        if i % 2 == 0 and ch.isalpha() is False:
            print('Illegal input')
            return False


def read_dictionary():
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    """
    global d
    with open(FILE, 'r') as f:
        for line in f:
            word = line.strip('\n')
            d[word] = word


def has_prefix(sub_s):
    """
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    global d
    for word in d:
        if d[word].startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
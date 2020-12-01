"""
The program calculates the sequence of printing pages for a book that consists of stitched notebooks.

Most printed books (especially hardcover books) consist of notebooks. Suppose that in a printing house the text is
printed on sheets of paper twice as large as the usual book format. Then these sheets are folded in half, from them
notebooks are formed, which are then sewn into a block. Stitched notebooks usually consist of 8, 12 or 16 sheets
(respectively 16, 24 or 32 pages) each.
"""


input_parameters = []
list_notebooks = []
notes_to_print = []
"""
input_parameters
Contains the number of pages for a book, the number of pages in a notebook, and a Boolean True or False for
separation of functionality.

list_notebooks
List of book pages distributed on a notebook

notes_to_print
List of notebooks ready for printing.
"""


def get_input():
    """
    Getting parameters from the user.
    :return: list
    """
    while True:
        try:
            quantity_pages_book = int(input('Please enter the quantity of pages in the book. Maximum 1280 pages: '))
            if 0 < quantity_pages_book < 1281:
                input_parameters.append(quantity_pages_book)
                break
            else:
                print('The quantity of pages in the book must be a positive integer number')
        except ValueError:
            print('Please don`t enter letter')

    while True:
        check_list = [16, 24, 32]
        try:
            quantity_pages_notebook = int(
                input('Please enter the quantity of pages in the notebook. Available options: 16, 24, 32 '))
            if quantity_pages_notebook in check_list and quantity_pages_book % quantity_pages_notebook == 0:
                input_parameters.append(quantity_pages_notebook)
                break
            else:
                print('Please enter one of the available options: 16, 24, 32 ')
        except ValueError:
            print('Please enter one of the available options: 16, 24, 32 ')

    while True:
        status_additional_function = int(input('Please enter the status additional function. 0 is Off, 1 is On '))
        if status_additional_function == 1 or status_additional_function == 0:
            input_parameters.append(status_additional_function)
            break
        else:
            print('Please enter 0 or 1. 0 is Off, 1 is On')

    return input_parameters


def get_notebooks(quantity_pages_book: int, quantity_pages_notebook: int) -> list:
    """
    We find out how many notebooks are in the book, taking into account the number of pages in the book and the
    number of pages in the notebook.
    :param quantity_pages_book: take from input_parameters [0]
    :param quantity_pages_notebook: take from input_parameters [1]
    :return: list
    """
    input_parameters[0] = quantity_pages_book
    input_parameters[1] = quantity_pages_notebook

    count_notebooks = int(input_parameters[0] / input_parameters[1])
    start = 1
    stop = input_parameters[1] + 1

    for i in range(1, count_notebooks + 1):
        note = list(range(start, stop))
        list_notebooks.append(note)
        start += input_parameters[1]
        stop += input_parameters[1]

    return list_notebooks


def count_notebooks():
    """
    The function prints out a list in which the pages of the book are grouped by notebooks.
    And the quantity of notebooks.
    :return: None
    """
    get_notebooks(input_parameters[0], input_parameters[1])
    print(list_notebooks, '\n' f'Quantity notebooks in this book: {len(list_notebooks)}')


def get_notes_to_print(quantity_pages_notebook: int) -> list:
    """
    The function generates a list of notebooks sorted by pages, taking into account the print queue.
    :param quantity_pages_notebook:
    :return: list
    """
    get_notebooks(input_parameters[0], input_parameters[1])
    ranges = int(quantity_pages_notebook / 4)
    n = 0
    for note in list_notebooks:
        one_note_to_print = []
        for j in range(1, ranges + 1):
            if n <= int(len(note) / 2):
                el = note[len(note) - 1 - n]
                one_note_to_print.append(el)
                el = note[n]
                one_note_to_print.append(el)
                n += 1
                el = note[n]
                one_note_to_print.append(el)
                el = note[len(note) - 1 - n]
                one_note_to_print.append(el)
                n += 1
        notes_to_print.append(one_note_to_print)
        n = 0

    return notes_to_print


def choose_status(flag: bool):
    """
    If the user entered:
    1 - the function displays a list of notebooks taking into account the print queue
    0 - the function displays a list of pages grouped by notebooks
    :param flag: bool from input_parameters[-1]
    :return: None
    """
    if flag:
        print(get_notes_to_print(input_parameters[1]))
    else:
        count_notebooks()


get_input()     # Calling input method.
choose_status(input_parameters[-1])     # Getting the result based on the entered data

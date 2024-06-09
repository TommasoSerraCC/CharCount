""" Analysis of Plato's 'The Republic'"""

import argparse
import os
import sys
import time
from loguru import logger
import matplotlib.pyplot as plt

def text_character_stats(text, args_parsed):
    """ This function handles a string and provides a quantitative descrisption about
        it's composition such as the frequencies of the characters or number of words,
        according to the options requested, registered in the namespace object 'args_parsed'"""

    # Option to cut the prologue and the conclusions
    if args_parsed.s:
        start_pos = text.index('continue to be to mankind the idea of good')
        end_pos = text.index('*** end of the project gutenberg ebook the republic ***')
        text = text[start_pos: end_pos]

    # Option to plot the barchart of the frequencies
    if args_parsed.t:
        character_list = 'abcdefghijklmnopqrstuvwxyz'
        character_dict = {}
        for character in character_list:
            character_dict[character] = 0
        for character in text:
            if character in character_list:
                character_dict[character] += 1

        plt.bar(character_dict.keys(),character_dict.values())
        plt.show()


def read_text_lower_case(filename):
    """ Reconstruct the full path to 'The Republic' by Plato, read the document
        and assign it to a string which is than returned in lowercase """
    # Reconstruct the full filepath
    filepath = os.path.join(os.getcwd(), filename)

    # Read the file and assign it to a string, logging an error message if the file is not found
    try:
        with open(filepath,'r',encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError as e:
        logger.error(f"The document doesn't exist. Verify the name inserted. {e}")
        # Stops the execution after the error message
        sys.exit(0)
    logger.info('Text file correctly opened')

    # Make all characters lowercase
    return text.lower()

if __name__ == '__main__':

    # Get the initial time
    start_time = time.time()

    # Initialize the parser
    parser = argparse.ArgumentParser(description=" Produce some stats about Plato's 'The Republic'")

    # Get the file name from command line
    parser.add_argument('filename',help='The name of the file containing The Republic')
    # Option to skip the useless parts
    parser.add_argument('-s',action='store_true',help='Option to skip prologue and conclusion')

    parser.add_argument('-t',action='store_true',help='Option to show the histogram')

    args = parser.parse_args()

    the_republic = read_text_lower_case(args.filename)
    text_character_stats(the_republic, args)

    # Print the total elapsed time
    end_time = time.time()
    logger.info(f'Total elapsed time {end_time-start_time}')

# %%
from tf.app import use
# import re
# import os
# import matplotlib.pyplot as plt
# import numpy as np

GNT = use('CenterBLC/N1904', version='1.0.0')
#GNT.api.F, GNT.api.L, GNT.api.T = GNT.api.F, GNT.api.L, GNT.api.T

# %% 1: generating INPUT
i=0
file=[]
selected_book = 'III_John'
outputfile_suffix = '_normalized'

for verse in GNT.api.F.otype.s('verse'):
    # text = "".join([GNT.api.F.translit.v(word) if not GNT.api.F.trailer.v(word) else GNT.api.F.translit.v(word)+" " for word in GNT.api.L.d(verse,'word')]).replace("_", " ")
    text = "".join([GNT.api.F.normalized.v(word) + " " for word in GNT.api.L.d(verse,'word')])
    bo, ch, ve = GNT.api.T.sectionFromNode(verse)
    final = "\t".join([bo, str(ch), str(ve), text.strip()])

    if bo == selected_book: # or 'John'
        file.append(final)
        if i<3:
            print(final)
        i=i+1

with open('./data_gnt/input_' + selected_book + outputfile_suffix, 'w', encoding='utf-8') as file:
    for line in file:
        file.write(line + '\n')

# %%
## stopped here: translate code # 2 into GNT equivalent with subphrases, and through this, generate the input file.


# %% 
# verse 3 John 1:1 == node 390213
s = GNT.api.T.sectionFromNode(390213)
print(s)
s = GNT.api.T.sectionTuple(390213)
print(s)


# %%
print(GNT.api.F.otype.v(390213))

# %%
# ran search query for 3 John 1:1, where received verse's node id
nodes = GNT.api.L.i(390213) # , otype="verse")
#print (len(nodes))
# print (nodes)
# found = [node for node in nodes if GNT.api.F.otype.v(node) == 'phrase']
# found = sorted([node for node in nodes if GNT.api.F.otype.v(node) == 'phrase'], key=lambda node: node)
# print (found)
found = [node for node in nodes if GNT.api.F.otype.v(node) == 'verse']
print (found)

# %% 3a-verse generating OUTPUT (via working with a specific verse directly)
i=0
file=[]
SELECTED_BOOK = 'III_John'
OUTPUTFILE_SUFFIX = '_normalized'
VERSE_ID = 390213 # for 3 John 1:1

# ran search query for 3 John 1:1, where received verse's node id
nodes_for_verse = GNT.api.L.i(VERSE_ID)
phrases_ofthe_verse = sorted([node for node in nodes_for_verse if GNT.api.F.otype.v(node) == 'phrase'], key=lambda node: node)

verse_text = ""
for phrase in phrases_ofthe_verse:
    phrase_text = " ".join([GNT.api.F.normalized.v(word) for word in GNT.api.L.d(phrase, 'word')])
    # phrase_text += "|" if phrase_text == 'W' else "| "
    phrase_text += "| "
    verse_text = verse_text + phrase_text

verse_text = verse_text.strip()
bo, ch, ve = GNT.api.T.sectionFromNode(VERSE_ID)
final = "\t".join([bo, str(ch), str(ve), verse_text.strip()])

if bo == SELECTED_BOOK:
    file.append(final)
    if i<3:
        print(final)
    i=i+1
    
with open('./data_gnt/output_' + SELECTED_BOOK + OUTPUTFILE_SUFFIX, 'w', encoding='utf-8') as file:
    for line in file:
        file.write(line + '\n')


# %%
s = GNT.api.T.sectionFromNode(137804)
print(s[0]) # indeed, 3 John book this is


# %% 3b-book generating OUTPUT (via working with a specific BOOK directly)
i=0
file=[]
SELECTED_BOOK = 'III_John'
OUTPUTFILE_SUFFIX = 'normalized'
# VERSE_ID = 390213 # for 3 John 1:1
BOOK_ID = 137804 # for 3 John
MODUS = 'clear' # 'XYs'
# MODUS = 'XYs'

# nodes_for_book = GNT.api.L.i(BOOK_ID)
verses_ofthe_Book = GNT.api.L.d(BOOK_ID, 'verse')

def to_groups_of_uninterrupted_sequences_present_or_missing_in (sequence_of_words) -> list[list[int]]:
    """
    Determines the grouping of contiguous numbers within the range defined by the first and last elements of the input list
    by indicating whether each number in the range is present in the list or missing. The function assumes that the input
    list (sequence_of_words) is sorted.
    It returns a
    list of groups, where each group is a list of consecutive numbers that share the same status (present in the input list
    or missing from it).
    Parameters:
        sequence_of_words (list[int]): A sorted list of integers representing positions or word identifiers.
    Returns:
        list[list[int]]:
            - A list of contiguous groups of numbers (each group being a list of integers) when there are missing numbers.
            The first group: integers from the phrase
            The second group: integers not from the phrase but before the continuation of the phrase's content
            The third group: integers from the phrase
            etc..
    """

    # sequence_of_words[0] gives the first element, and sequence_of_words[-1] gives the last element of the list.
    full_range = list(range(sequence_of_words[0], sequence_of_words[-1] + 1))
    # if there are no missing numbers, return False
    if len(sequence_of_words) == len(full_range):
        return False
    groups = []
    current_group = []
    current_type = None  # True if number is present, False if missing
    for num in full_range:
        if current_type is None:
            current_type = (num in sequence_of_words)
            current_group.append(num)
        else:
            num_type = (num in sequence_of_words)
            if num_type == current_type:
                current_group.append(num)
            else:
                groups.append(current_group)
                current_group = [num]
                current_type = num_type
    if current_group:
        groups.append(current_group)
    return groups

def add_sequential_chunk_to_verse(verse_text, MODUS, unused_words_ofthe_verse, sequence_of_words): # sequence_of_words must be uninterrupted sequence of integers 

    if (len(sequence_of_words) > 0) and any(word in unused_words_ofthe_verse for word in sequence_of_words): # only the words that are still unused can be used for building new sub-phrases. they could have been used previously for building new-subphrases in the cases of phrases within breaking-phrases of GNT.

        if (MODUS == 'clear'):
            phrase_text = " ".join([GNT.api.F.normalized.v(word) for word in sequence_of_words])
            phrase_text += "| "
            verse_text = verse_text + phrase_text
                
        if (MODUS == 'XYs'):
            phrase_text = "".join(["X"] * (len(sequence_of_words) - 1))
            phrase_text += "Y"
            verse_text = verse_text + phrase_text

        unused_words_ofthe_verse = [w for w in unused_words_ofthe_verse if w not in sequence_of_words]

    return verse_text,unused_words_ofthe_verse

def add_chunk_to_verse(verse_text, MODUS, unused_words_ofthe_verse, sequence_of_words): # sequence_of_words can be interrupted sequence of integers, as can happen within a phrase

    if (len(sequence_of_words) > 0):

        groups_of_prospective_new_subphrases = to_groups_of_uninterrupted_sequences_present_or_missing_in(sequence_of_words) # can only occur within a phrase
        if groups_of_prospective_new_subphrases:
            is_from_phrase = True
            for subgroup in groups_of_prospective_new_subphrases:
                if (is_from_phrase):
                    verse_text, unused_words_ofthe_verse = add_sequential_chunk_to_verse(
                        verse_text, MODUS, unused_words_ofthe_verse, subgroup
                    )
                else: # assuming that each intercalating member is its own new-subphrase
                    for single in subgroup:
                        verse_text, unused_words_ofthe_verse = add_sequential_chunk_to_verse(
                            verse_text, MODUS, unused_words_ofthe_verse, [single]
                        )
                is_from_phrase = not is_from_phrase # the from-phrase groups and not-from-phrase groups follow each other sequentially
        else:
            verse_text, unused_words_ofthe_verse = add_sequential_chunk_to_verse(
                verse_text, MODUS, unused_words_ofthe_verse, sequence_of_words
            )

    return verse_text,unused_words_ofthe_verse

for verse in verses_ofthe_Book:

    phrases_ofthe_verse = GNT.api.L.d(verse, 'phrase')
    words_ofthe_verse = GNT.api.L.d(verse, 'word')
    unused_words_ofthe_verse = list(words_ofthe_verse)

    verse_text = ""
    for phrase in phrases_ofthe_verse:

        words_for_phrase = GNT.api.L.d(phrase, 'word')  # words_for_phrase implements collections.abc.Sequence, as does range
        if (unused_words_ofthe_verse[0] < words_for_phrase[0]): # make a new-subphrase of the "orphan" words (those not in a phrase)

            range_of_orphan_words = range(unused_words_ofthe_verse[0], words_for_phrase[0])
            # orphans inside the verse
            verse_text, unused_words_ofthe_verse = add_chunk_to_verse(verse_text, MODUS, unused_words_ofthe_verse, range_of_orphan_words)

        # core phrase's words
        verse_text, unused_words_ofthe_verse = add_chunk_to_verse(verse_text, MODUS, unused_words_ofthe_verse, words_for_phrase)

    if (len(unused_words_ofthe_verse) > 0):
        # orphans at the end of the verse, after all the phrases
        verse_text, unused_words_ofthe_verse = add_chunk_to_verse(verse_text, MODUS, unused_words_ofthe_verse, unused_words_ofthe_verse)

    verse_text = verse_text.strip()
    bo, ch, ve = GNT.api.T.sectionFromNode(verse)
    final = "\t".join([bo, str(ch), str(ve), verse_text.strip()])

    # if bo == SELECTED_BOOK:
    file.append(final)
    if i<3:
        print(final)
    i=i+1
    
with open('./data_gnt/output_' + SELECTED_BOOK + "_" + OUTPUTFILE_SUFFIX + "_" + MODUS, 'w', encoding='utf-8') as file:
    for line in file:
        file.write(line + '\n')

print('done')

# %%
books = GNT.api.F.otype.s('book')
print (books)

# %% 3c-NT generating OUTPUT (via working with whole NT)
i=0
file_contents=[]
# SELECTED_BOOK = 'III_John'
OUTPUTFILE_SUFFIX = 'normalized'
# VERSE_ID = 390213 # for 3 John 1:1
# BOOK_ID = 137804 # for 3 John
MODUS = 'clear' # 'XYs'
# MODUS = 'XYs'

books = GNT.api.F.otype.s('book')

def to_groups_of_uninterrupted_sequences_present_or_missing_in (sequence_of_words) -> list[list[int]]:
    """
    Determines the grouping of contiguous numbers within the range defined by the first and last elements of the input list
    by indicating whether each number in the range is present in the list or missing. The function assumes that the input
    list (sequence_of_words) is sorted.
    It returns a
    list of groups, where each group is a list of consecutive numbers that share the same status (present in the input list
    or missing from it).
    Parameters:
        sequence_of_words (list[int]): A sorted list of integers representing positions or word identifiers.
    Returns:
        list[list[int]]:
            - A list of contiguous groups of numbers (each group being a list of integers) when there are missing numbers.
            The first group: integers from the phrase
            The second group: integers not from the phrase but before the continuation of the phrase's content
            The third group: integers from the phrase
            etc..
    """

    # sequence_of_words[0] gives the first element, and sequence_of_words[-1] gives the last element of the list.
    full_range = list(range(sequence_of_words[0], sequence_of_words[-1] + 1))
    # if there are no missing numbers, return False
    if len(sequence_of_words) == len(full_range):
        return False
    groups = []
    current_group = []
    current_type = None  # True if number is present, False if missing
    for num in full_range:
        if current_type is None:
            current_type = (num in sequence_of_words)
            current_group.append(num)
        else:
            num_type = (num in sequence_of_words)
            if num_type == current_type:
                current_group.append(num)
            else:
                groups.append(current_group)
                current_group = [num]
                current_type = num_type
    if current_group:
        groups.append(current_group)
    return groups

def add_sequential_chunk_to_verse(verse_text, unused_words_ofthe_verse, sequence_of_words): # sequence_of_words must be uninterrupted sequence of integers 

    if (len(sequence_of_words) > 0) and any(word in unused_words_ofthe_verse for word in sequence_of_words): # only the words that are still unused can be used for building new sub-phrases. they could have been used previously for building new-subphrases in the cases of phrases within breaking-phrases of GNT.

        if (MODUS == 'clear'):
            phrase_text = " ".join([GNT.api.F.normalized.v(word) for word in sequence_of_words])
            phrase_text += "| "
            verse_text = verse_text + phrase_text
                
        if (MODUS == 'XYs'):
            phrase_text = "".join(["X"] * (len(sequence_of_words) - 1))
            phrase_text += "Y"
            verse_text = verse_text + phrase_text

        unused_words_ofthe_verse = [w for w in unused_words_ofthe_verse if w not in sequence_of_words]

    return verse_text,unused_words_ofthe_verse

def add_chunk_to_verse(verse_text, unused_words_ofthe_verse, sequence_of_words): # sequence_of_words can be interrupted sequence of integers, as can happen within a phrase

    if (len(sequence_of_words) > 0):

        groups_of_prospective_new_subphrases = to_groups_of_uninterrupted_sequences_present_or_missing_in(sequence_of_words) # can only occur within a phrase
        if groups_of_prospective_new_subphrases:
            is_from_phrase = True
            for subgroup in groups_of_prospective_new_subphrases:
                if (is_from_phrase):
                    verse_text, unused_words_ofthe_verse = add_sequential_chunk_to_verse(
                        verse_text, unused_words_ofthe_verse, subgroup
                    )
                else: # assuming that each intercalating member is its own new-subphrase
                    for single in subgroup:
                        verse_text, unused_words_ofthe_verse = add_sequential_chunk_to_verse(
                            verse_text, unused_words_ofthe_verse, [single]
                        )
                is_from_phrase = not is_from_phrase # the from-phrase groups and not-from-phrase groups follow each other sequentially
        else:
            verse_text, unused_words_ofthe_verse = add_sequential_chunk_to_verse(
                verse_text, unused_words_ofthe_verse, sequence_of_words
            )

    return verse_text,unused_words_ofthe_verse

def handle_book(book, i):
    verses_ofthe_Book = GNT.api.L.d(book, 'verse')
    for verse in verses_ofthe_Book:
        phrases_ofthe_verse = GNT.api.L.d(verse, 'phrase')
        words_ofthe_verse = GNT.api.L.d(verse, 'word')
        unused_words_ofthe_verse = list(words_ofthe_verse)

        verse_text = ""
        for phrase in phrases_ofthe_verse:
            phrases_within_phrase = GNT.api.L.d(phrase, 'phrase')
            if (len(phrases_within_phrase) > 0):
                phrases_to_process = phrases_within_phrase
            else: # == 0
                phrases_to_process = [phrase]

            for phr_within_phrase in phrases_to_process: # might be just one parent phrase
                words_for_phrase = GNT.api.L.d(phr_within_phrase, 'word')  # words_for_phrase implements collections.abc.Sequence, as does range
                if (len(unused_words_ofthe_verse) > 0): 
                    if (unused_words_ofthe_verse[0] < words_for_phrase[0]): # make a new-subphrase of the "orphan" words (those not in a phrase)
                        range_of_orphan_words = range(unused_words_ofthe_verse[0], words_for_phrase[0])
                        # orphans inside the verse
                        verse_text, unused_words_ofthe_verse = add_chunk_to_verse(verse_text, unused_words_ofthe_verse, range_of_orphan_words)

                    # core phrase's words
                    verse_text, unused_words_ofthe_verse = add_chunk_to_verse(verse_text, unused_words_ofthe_verse, words_for_phrase)

        if (len(unused_words_ofthe_verse) > 0):
        # orphans at the end of the verse, after all the phrases
            verse_text, unused_words_ofthe_verse = add_chunk_to_verse(verse_text, unused_words_ofthe_verse, unused_words_ofthe_verse)

        verse_text = verse_text.strip()
        bo, ch, ve = GNT.api.T.sectionFromNode(verse)
        final = "\t".join([bo, str(ch), str(ve), verse_text.strip()])

    # if bo == SELECTED_BOOK:
        file_contents.append(final)
        # if i<3:
        print(final)
        # i=i+1


for book in books:
    a = 1
    handle_book(book, i)
    
    
with open('./data_gnt/output_NT_' + OUTPUTFILE_SUFFIX + "_" + MODUS, 'w', encoding='utf-8') as file:
    for line in file_contents:
        file.write(line + '\n')

print('done')


# %% 4 counting words in input and output files if they are equal
# sergp
def count_words_in_line(file_lines: list[str], line_number: int) -> int:
    """
    Counts the number of words in the specified line from a list of lines.

    Args:
        file_lines (list[str]): A list of strings, each representing a line from a text file.
        line_number (int): The line number to count the words in (1-indexed).

    Returns:
        int: The number of words in the specified line.
    """
    try:
        # Access the specified line (adjusting for 1-indexing)
        line = file_lines[line_number - 1]
        # Remove leading and trailing whitespace from the line
        line = line.strip()
        # Split the line into words using whitespace as delimiters
        words = line.split()
        # Return the number of words
        return len(words)
    except IndexError:
        print(f"Error: Line {line_number} does not exist in the file.")
        return 0

inputfilePath = "./data_gnt/input_III_John_normalized"
# inputfilePath = "./data_gnt/input_III_John"
outputfilePath = "./data_gnt/output_III_John_normalized_clear"

with open(inputfilePath, 'r', encoding='utf-8') as fi, open(outputfilePath, 'r', encoding='utf-8') as fo:

    lines_fi = fi.readlines()
    lines_fo = fo.readlines()

    for i in range(1,16):
        word_count_line_input = count_words_in_line(lines_fi, i)
        word_count_line_output = count_words_in_line(lines_fo, i)

        if word_count_line_input != word_count_line_output:
            print(f"Line {i} of file {inputfilePath} contains {word_count_line_input} words.")
            print(f"Line {i} of file {outputfilePath} contains {word_count_line_output} words.\n")

        i=i+1

print ('done')

# %% 6: generating OUTPUT (via parsing the whole NT, but take previous code for more targeted approach)
i=0
file=[]
selected_book = 'III_John'
outputfile_suffix = '_normalized'

for verse in GNT.api.F.otype.s('verse'):
    verse_text = ""
    phrases = GNT.api.L.d(verse,'phrase')
    for phrase in phrases:
        phrase_text = "".join([GNT.api.F.normalized.v(word) for word in GNT.api.L.d(phrase, 'word')])
        # phrase_text += "|" if phrase_text == 'W' else "| "
        phrase_text += "| "
        
        # Genesis	39	23	>JN FR BJT HSHR R>H >T KL M>WMH BJDW| B>CR JHWH >TW| W|>CR HW> <FH| JHWH MYLJX|

        # text = []
        # for word in GNT.api.L.d(subphrase, 'word'):
        #     if not GNT.api.F.trailer.v(word):
        #         text.append(GNT.api.F.g_cons.v(word))
        #     else:
        #         text.append(GNT.api.F.g_cons.v(word) + " ")
        # phrase_text = "".join(text)
        # phrase_text = phrase_text.replace("_"," ")
        # phrase_text = phrase_text.strip()
        # if phrase_text == 'W':
        #     phrase_text += "|"
        # else:
        #     phrase_text += "| "
        
        verse_text = verse_text + phrase_text

    verse_text = verse_text.strip()
    bo, ch, ve = GNT.api.T.sectionFromNode(verse)
    final = "\t".join([bo, str(ch), str(ve), verse_text.strip()])

    # if bo == 'Genesis' and str(ch) == '7' and str(ve) == '16':
    #     if i<10:
    #         print(final)
    #     i=i+1
    
    if bo == selected_book: # or 'John'
        file.append(final)
        if i<3:
            print(final)
        i=i+1
    
    # if bo == 'Genesis':
    #     file_input.append(final)

with open('./data_gnt/output_' + selected_book + outputfile_suffix, 'w', encoding='utf-8') as file:
    for line in file:
        file.write(line + '\n')
# %%

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
file_input=[]
selected_book = 'III_John'
outputfile_suffix = '_normalized'

for verse in GNT.api.F.otype.s('verse'):
    # text = "".join([GNT.api.F.translit.v(word) if not GNT.api.F.trailer.v(word) else GNT.api.F.translit.v(word)+" " for word in GNT.api.L.d(verse,'word')]).replace("_", " ")
    text = "".join([GNT.api.F.normalized.v(word) + " " for word in GNT.api.L.d(verse,'word')])
    bo, ch, ve = GNT.api.T.sectionFromNode(verse)
    final = "\t".join([bo, str(ch), str(ve), text.strip()])

    if bo == selected_book: # or 'John'
        file_input.append(final)
        if i<3:
            print(final)
        i=i+1

with open('./data_gnt/input_' + selected_book + outputfile_suffix, 'w', encoding='utf-8') as file:
    for line in file_input:
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

# %% 2 generating OUTPUT (via working with a specific verse directly)
i=0
file_input=[]
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
    file_input.append(final)
    if i<3:
        print(final)
    i=i+1
    
with open('./data_gnt/output_' + SELECTED_BOOK + OUTPUTFILE_SUFFIX, 'w', encoding='utf-8') as file:
    for line in file_input:
        file.write(line + '\n')


# %%
s = GNT.api.T.sectionFromNode(137804)
print(s[0]) # indeed, 3 John book this is


# %% 3 generating OUTPUT (via working with a specific BOOK directly)
i=0
file_input=[]
SELECTED_BOOK = 'III_John'
OUTPUTFILE_SUFFIX = '_normalized'
# VERSE_ID = 390213 # for 3 John 1:1
BOOK_ID = 137804 # for 3 John

# nodes_for_book = GNT.api.L.i(BOOK_ID)
verses_ofthe_Book = GNT.api.L.d(BOOK_ID, 'verse')

for verse in verses_ofthe_Book:

    phrases_ofthe_verse = GNT.api.L.d(verse, 'phrase')
    words_ofthe_verse = GNT.api.L.d(verse, 'word')
    unused_words_ofthe_verse = list(words_ofthe_verse)

    verse_text = ""
    for phrase in phrases_ofthe_verse:

        words_for_phrase = GNT.api.L.d(phrase, 'word')
        if (unused_words_ofthe_verse[0] < words_for_phrase[0]): # anomaly scenario: make a phrase of the "orphan" words (those not in a phrase)

            # in Python, range excludes the last element!
            range_of_orphan_words = range(unused_words_ofthe_verse[0], words_for_phrase[0])
            phrase_text = " ".join([GNT.api.F.normalized.v(word) for word in range_of_orphan_words])
            phrase_text += "| "
            verse_text = verse_text + phrase_text

            unused_words_ofthe_verse = [w for w in unused_words_ofthe_verse if w not in range_of_orphan_words]

        # do this in any case for each regular phrase (unused_words_ofthe_verse[0] == words_for_phrase[0])
        phrase_text = " ".join([GNT.api.F.normalized.v(word) for word in words_for_phrase])
        phrase_text += "| "
        verse_text = verse_text + phrase_text

        unused_words_ofthe_verse = [w for w in unused_words_ofthe_verse if w not in words_for_phrase]

    verse_text = verse_text.strip()
    bo, ch, ve = GNT.api.T.sectionFromNode(verse)
    final = "\t".join([bo, str(ch), str(ve), verse_text.strip()])

    # if bo == SELECTED_BOOK:
    file_input.append(final)
    if i<3:
        print(final)
    i=i+1
    
with open('./data_gnt/output_' + SELECTED_BOOK + OUTPUTFILE_SUFFIX, 'w', encoding='utf-8') as file:
    for line in file_input:
        file.write(line + '\n')

print('done')

# %% 4: generating OUTPUT (via parsing the whole NT, but take previous code for more targeted approach)
i=0
file_input=[]
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
        file_input.append(final)
        if i<3:
            print(final)
        i=i+1
    
    # if bo == 'Genesis':
    #     file_input.append(final)

with open('./data_gnt/output_' + selected_book + outputfile_suffix, 'w', encoding='utf-8') as file:
    for line in file_input:
        file.write(line + '\n')
# %%

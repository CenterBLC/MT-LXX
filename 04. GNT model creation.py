# %%
from tf.app import use
# import re
# import os
# import matplotlib.pyplot as plt
# import numpy as np

GNT = use('CenterBLC/N1904', version='1.0.0')
Fgnt, Lgnt, Tgnt = GNT.api.F, GNT.api.L, GNT.api.T

# %% 1
i=0
file_input=[]
selected_book = 'III_John'
outputfile_suffix = '_normalized'

for verse in Fgnt.otype.s('verse'):
    # text = "".join([Fgnt.translit.v(word) if not Fgnt.trailer.v(word) else Fgnt.translit.v(word)+" " for word in Lgnt.d(verse,'word')]).replace("_", " ")
    text = "".join([Fgnt.normalized.v(word) + " " for word in Lgnt.d(verse,'word')])
    bo, ch, ve = Tgnt.sectionFromNode(verse)
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

# %% 2
i=0
file_input=[]
selected_book = 'III_John'
outputfile_suffix = '_normalized'

for verse in Fgnt.otype.s('verse'):
    verse_text = ""
    subphrases = Lgnt.d(verse,'subphrase')
    for subphrase in subphrases:
        subphrase_text = "".join([Fgnt.normalized.v(word) for word in Lgnt.d(subphrase, 'word')])
        # subphrase_text += "|" if subphrase_text == 'W' else "| "
        subphrase_text += "| "
        
        # Genesis	39	23	>JN FR BJT HSHR R>H >T KL M>WMH BJDW| B>CR JHWH >TW| W|>CR HW> <FH| JHWH MYLJX|

        # text = []
        # for word in Lgnt.d(subphrase, 'word'):
        #     if not Fgnt.trailer.v(word):
        #         text.append(Fgnt.g_cons.v(word))
        #     else:
        #         text.append(Fgnt.g_cons.v(word) + " ")
        # subphrase_text = "".join(text)
        # subphrase_text = subphrase_text.replace("_"," ")
        # subphrase_text = subphrase_text.strip()
        # if subphrase_text == 'W':
        #     subphrase_text += "|"
        # else:
        #     subphrase_text += "| "
        
        verse_text = verse_text + subphrase_text

    verse_text = verse_text.strip()
    bo, ch, ve = Tgnt.sectionFromNode(verse)
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

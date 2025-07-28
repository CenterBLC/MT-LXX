# %%
from tf.advanced.display import loadCss
from tf.advanced.display import displayReset
from tf.app import use
GNT = use('CenterBLC/N1904', version='1.0.0', hoist=globals()) # hoist globals will inject CSS in HTML results
# Fgnt, Lgnt, Tgnt = GNT.api.F, GNT.api.L, GNT.api.T


# %%
# sph = GNT.structureStrFromNode(266538)
#sph = GNT.nodeFromSectionStr("Matthew 1:1")

# book = A.nodeFromSectionStr("Genesis")
# s = L.d(book, otype="sentence")[0]
# A.pretty(s)

# from IPython.display import display, HTML
# display(HTML(self.cssDefault))
# GNT.displayInit()

# %%
# loadCss(GNT)    
displayReset(GNT)
loadCss(GNT)
# GNT.displaySetup(withNodes=True, standardFeatures=True, hiddenTypes={"clause", "phrase", "wg", "subphrase"}, hideTypes=True) # original displaySetup
# GNT.displaySetup(withNodes=True, standardFeatures=True, hiddenTypes={"clause", "phrase", "wg"}, hideTypes=True)
GNT.displaySetup(withNodes=True, standardFeatures=True, hideTypes=True, baseTypes={"clause"}, condensed=True)

for i in range(266536, 266549): # range for Mat 1:1
    print(str(i) + "   " + GNT.api.F.otype.v(i))
    GNT.pretty(i)
# i = 266539
# print(str(i) + "   " + GNT.api.F.otype.v(i))
# GNT.pretty(i)



# %%
#displayReset(GNT)
loadCss(GNT)


John1_1 = '''
book book=John
 chapter chapter=1 
   verse verse=1
    word lemma
'''
John1_1  = GNT.search(John1_1)
GNT.show(John1_1, start=1, end=1, multiFeatures=False, condensed=True)


# %% 🔹 1. Verify that clause nodes really exist
clause_nodes = [n for n in GNT.api.F.otype.s('clause')]
print(f"Number of clause nodes: {len(clause_nodes)}")
# Number of clause nodes: 42506

# %%
loadCss(GNT)

# results = GNT.search("""
# verse book=Matthew chapter=1 verse=1
#     word lemma
# """)
results = GNT.search("""
book book=Matthew
    chapter chapter=1
        verse verse=2
            word lemma
""")

GNT.show(results, start=1, end=1000, condensed=True, multiFeatures=False, hiddenTypes={"wg", "subphrase"}, hideTypes=True, queryFeatures=False, withNodes=True)


# %%
# Mat 1:1 verse id is 382714
GNT.pretty(382714, condensed=False, multiFeatures=False, hiddenTypes={"wg", "subphrase"}, hideTypes=True, queryFeatures=False, withNodes=True)

# %%
loadCss(GNT)
# First clause id is 138067 -- not found in Mat 1:1, but first in Mat 1:2!!!
GNT.pretty(138067, condensed=False, multiFeatures=False, hiddenTypes={"wg", "subphrase"}, hideTypes=True, queryFeatures=False, withNodes=True)

# %%

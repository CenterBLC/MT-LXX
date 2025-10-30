# def run_all():
# %%
from tf.app import use
import sys
color = {1: "#47edff", 2: "#81ee93", 3: "#eaff47", 4: "#ffcb47", 5: "#ffa647", 6: "#ff7b47", 7: "#ff479d", 8: "#ff4747", 9: "#477eff", 10: "#a647ff"}

# %%
# The TF files from conversion at step "01" have been uploaded to sergpanf/LXX-Link-P; they are also found in this project under tf/0.0.8 folder
A = use("sergpanf/LXX-Link-P", version="0.0.8", hoist=globals())

# %%
# A.footprint()
F.otype.s("error")

# %%
for b in F.otype.s("book"):
    print(f"{b} {A.sectionStrFromNode(b)}")

# %%
# "cls" is a local FEATURE !
F.cls.freqList(nodeTypes={"word"})

# %%
F.sp.freqList(nodeTypes={"word"})

# %%
F.lemma.freqList(nodeTypes={"word"})

# %%
F.lemma.freqList()

# %%
F.cls.freqList(nodeTypes={"wg"})

# %%
F.cls.freqList(nodeTypes={"clause"})

# %%
F.cls.freqList(nodeTypes={"phrase"})

# %%
# to enalbe the display of nodes correctly, change it
A.displaySetup(withNodes=True, standardFeatures=True, hiddenTypes={"clause", "phrase", "wg", "subphrase"}, hideTypes=True)
# A.displaySetup(withNodes=True, standardFeatures=True)
# currently, will not show all nodes
book = A.nodeFromSectionStr("Genesis")
s = L.d(book, otype="sentence")[0]
A.pretty(s)

# %%
# research mode
book = A.nodeFromSectionStr("Genesis")
s = L.d(book, otype="wg")[0]
A.pretty(s)

# %%
# end user mode
results = A.search("""
verse book=Genesis
    sentence
        word
""")
A.show(results, end=2, condensed=True, multiFeatures=False, queryFeatures=True, withNodes=True)

# %%
# end user mode
results = A.search("""
word greek*
""")
A.show(results, end=2, condensed=True, multiFeatures=False, queryFeatures=True, withNodes=True)

# %%
# end user mode
results = A.search("""
word greek*
""")
A.show(results, end=2, condensed=True, multiFeatures=False, queryFeatures=True, withNodes=True, hiddenTypes={"wg"})

# %%
# end user mode
results = A.search("""
word greek*
""")
A.show(results, end=1, condensed=True, multiFeatures=True, queryFeatures=True, withNodes=True, hiddenTypes={"wg"})


# run_all()

# %%

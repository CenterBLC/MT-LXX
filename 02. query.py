# %%
from tf.app import use
color = {1: "#47edff", 2: "#81ee93", 3: "#eaff47", 4: "#ffcb47", 5: "#ffa647", 6: "#ff7b47", 7: "#ff479d", 8: "#ff4747", 9: "#477eff", 10: "#a647ff"}

# %%
# for using LXX-Link-P (Public repository), use the following line
# A = use("sergpanf/LXX-Link-P", version="0.0.1")
A = use("sergpanf/LXX-Link:clone", version="0.0.1", checkout="clone", hoist=globals(), backend="TF.Convert.XML_BackEnd")

# %%
A.footprint()

# %%
F.otype.s("error")

# %%
for b in F.otype.s("book"):
    print(f"{b} {A.sectionStrFromNode(b)}")

# %%
F.cls.freqList(nodeTypes={"word"})

# %%
F.cls.freqList(nodeTypes={"wg"})

# %%
F.cls.freqList(nodeTypes={"clause"})

# %%
F.cls.freqList(nodeTypes={"phrase"})

# %%
# to enalbe the display of nodes correctly, change it
A.displaySetup(withNodes=True, standardFeatures=True, hiddenTypes={"clause", "phrase"}, hideTypes=True)
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


# %%

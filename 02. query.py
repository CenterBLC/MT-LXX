# %%
# from tf.convert.xml import XML
# from lowfat_sergpanf_2025_02_09_vstudioVer import convertTaskCustom
#from tf.advanced.helpers import dm
#from tf.advanced.zipdata import zipAll, addCheckout
from tf.app import use
#color = {1: "#47edff", 2: "#81ee93", 3: "#eaff47", 4: "#ffcb47", 5: "#ffa647", 6: "#ff7b47", 7: "#ff479d", 8: "#ff4747", 9: "#477eff", 10: "#a647ff"}


# %%
A = use("sergpanf/LXX-Link:clone", backend="TF.Convert.XML_BackEnd", checkout="clone", hoist=globals())


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
book = A.nodeFromSectionStr("I_Timothy")
s = L.d(book, otype="sentence")[0]
A.pretty(s)

# %%
# research mode
book = A.nodeFromSectionStr("I_Timothy")
s = L.d(book, otype="wg")[0]
A.pretty(s)

# %%
# end user mode
results = A.search("""
verse book=I_Timothy
    sentence
        word
""")
A.show(results, end=2, condensed=True, multiFeatures=False, queryFeatures=True, withNodes=True)


# %%

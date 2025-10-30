# %%
from tf.convert.xml import XML
from lowfat_simplified import convertTaskCustom

keywordAtts = set(
    """
    case
    class
    number
    gender
    mood
    person
    role
    tense
    type
    voice
    degree
    articular
""".strip().split()
)

trimAtts = set(
    """
    domain
    frame
    gloss
    id
    lemma
    ln
    morph
    normalized
    ref
    referent
    rule
    strong
    subjref
    unicode
""".strip().split()
)

# 
renameAtts = {
    "Rule": "crule",
    "frame": "framespec",
    "subjref": "subjrefspec",
    "class": "cls",
    "type": "typems",
}

# 
X = XML(
    convertTaskCustom=convertTaskCustom,
    keywordAtts=keywordAtts,
    trimAtts=trimAtts,
    renameAtts=renameAtts,
    verbose=1,
    xml="2025-04-24",
    tf="0.0.8"
)

X.task(check=True)
X.task(convert=True)
X.task(load=True)
X.task(app=True)
# %%

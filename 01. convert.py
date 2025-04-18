# %%
#%load_ext autoreload
#%autoreload 2 

import os
import sys
current_working_dir = os.getcwd()
sys.path.append(current_working_dir)
# Deduplicate sys.path, preserving order
sys.path = list(dict.fromkeys(sys.path))
#print(sys.path)
import importlib
module_name = "lowfat_sergpanf_2025_02_09_vstudioVer"
module = importlib.import_module(module_name)
importlib.reload(module)

#  
from tf.convert.xml import XML
from lowfat_sergpanf_2025_02_09_vstudioVer import convertTaskCustom
#from tf.advanced.helpers import dm
#from tf.advanced.zipdata import zipAll, addCheckout
#from tf.app import use
#color = {1: "#47edff", 2: "#81ee93", 3: "#eaff47", 4: "#ffcb47", 5: "#ffa647", 6: "#ff7b47", 7: "#ff479d", 8: "#ff4747", 9: "#477eff", 10: "#a647ff"}


# 
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
    xml="2025-04-17",
    tf="0.0.3"
)

X.task(check=True)
X.task(convert=True)
X.task(load=True)
X.task(app=True)
# %%

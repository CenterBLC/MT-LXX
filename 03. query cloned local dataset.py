# %%
from tf.app import use
import sys

# %%
# all three works and produce same result which passes all tests from "02. query.py"
A = use("sergpanf/LXX-Link-P:clone", version="0.0.8", checkout="clone", hoist=globals())   
A = use("app:~/github/sergpanf/LXX-Link-P/app", version="0.0.8", hoist=globals())
A = use("app:~/github/sergpanf/LXX-Link-P/app", locations="H:/My Drive/eduAndrews/_WORK/TF_Projects_VS/github/sergpanf/LXX-Link-P/tf", version="0.0.8", hoist=globals())

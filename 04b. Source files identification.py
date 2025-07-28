# %%
from tf.app import use
A = use('CenterBLC/N1904', version='1.0.0', hoist=globals())

# %%
# print(A.__class__)
print(A.__class__.__module__)
print(A.__class__.__name__)
print(A.__class__.__module__)

# print(A.displaySetup.__module__)
# # %%
# print(A.displaySetup.__doc__)
# # %%
# print(A.displaySetup)

# %%
print(A.displaySetup.__func__.__code__.co_filename) # gives the full path to the module folder. from that, chk 1Note doc reg. reading those files from 2025-07-10, 21-25...
print(A.__class__.__module__) # output: tf.apps.CenterBLC/N1904.app, meaning look in text-fabric-data folder

# %%
print(A.show.__func__.__code__.co_filename)
print(A.pretty.__func__.__code__.co_filename)



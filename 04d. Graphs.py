# %% example of multi-y plot
import matplotlib.pyplot as plt

x1 = [0,1,2,3,4,5]
y1 = [0,1,4,9,16,25]      # quadratic
y2 = [0,1,2,3,4,5]        # linear
y3 = [0,10,100,1000,10000,100000]  # exponential

fig, ax1 = plt.subplots()

ax2 = ax1.twinx()   # second y-axis
ax3 = ax1.twinx()   # third y-axis

# Offset the third axis to the right
ax3.spines["right"].set_position(("axes", 1.2))

ax1.plot(x1, y1, 'b-')
ax2.plot(x1, y2, 'g-')
ax3.plot(x1, y3, 'r-')

ax1.set_xlabel("X axis")
ax1.set_ylabel("y1 quadratic", color='b')
ax2.set_ylabel("y2 linear", color='g')
ax3.set_ylabel("y3 exponential", color='r')

plt.show()

# %% F-Scores visualization
import matplotlib.pyplot as plt

x1 = ['normalized','translit','norm+transl','norm<m>transl','nmt+llt','nmt+llt+cgp', 'NLCM', 'IDEAL']
y1 = [93.20,91.71,92.74,92.66,93.59,94.20,94.63,100.00]   # F-score
y2 = [91.77,89.39,91.76,91.93,93.02,93.08,93.32,100.00]   # Precision
y3 = [94.67,94.14,93.73,93.40,94.16,95.34,95.97,100.00]   # Recall

fig, ax1 = plt.subplots()
ax1.grid(True, which="both", axis="both", linestyle="--", alpha=0.7)
plt.xticks(rotation=20, ha="right")   # 45° angle, aligned to the right

ax2 = ax1.twinx()   # second y-axis
ax3 = ax1.twinx()   # third y-axis

# Offset the third axis to the right
ax3.spines["right"].set_position(("axes", 1.2))

ax1.plot(x1, y1, 'b-')
ax2.plot(x1, y2, 'g-')
ax3.plot(x1, y3, 'r-')

ax1.set_xlabel("AI Training Experiments")
ax1.set_ylabel("F-Score", color='b')
ax2.set_ylabel("Precision", color='g')
ax3.set_ylabel("Recall", color='r')

# --- Add Y-values above each point ---
# --- Add Y-values with different offsets ---
offsets = {
    "A": -0.5,      # add +1 for Dataset A
    "B": 0,    # add +0.1 for Dataset B
    "C": 0.75      # add +20 for Dataset C
}

for x, y in zip(x1, y1):
    ax1.text(x, y + offsets["A"], f"{y}", color="b", ha="center", va="bottom", fontsize=8)

for x, y in zip(x1, y2):
    ax2.text(x, y + offsets["B"], f"{y}", color="g", ha="center", va="bottom", fontsize=8)

for x, y in zip(x1, y3):
    ax3.text(x, y + offsets["C"], f"{y}", color="r", ha="center", va="bottom", fontsize=8)

description = (
    "normalized: Accented Greek Text (βίβλος)\n"
    "translit: Transliteration, Non-Accented (Biblos)\n"
    "norm+transl: Accented, Followed by Non-Accented (βίβλος_Biblos)\n"
    "norm<m>transl: Accented, Merged with Non-Accented (βBίiβbλlοoςs)\n"
    "nmt+llt: norm<m>transl Followed by lemma<m>lemmatransl (ἐeγgέeνnνnηeσsεeνn_γgεeνnνnάaωo)\n"
    "nmt+llt+cgp: ... Followed by case, gender, person (ΒBίiβbλlοoςs_βbίiβbλlοoςs_nominative_feminine)\n"
    "NLCM: ... Followed by mood, sp, tense, morph (ἐeπpοoίiηeσsεeνn_πpοoιiέeωo_p_3_indicative_verbaoristV-AAI-3S)\n"
    "\n"
)
plt.figtext(0.5, -0.1, description, wrap=True, ha="center", va="top", fontsize=9)
plt.show()
# %%

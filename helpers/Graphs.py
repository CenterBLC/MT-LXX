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

# %%

data = [ # nr. 4 and 6 and 8 are out of the game (in blue or commented out)
    {'name': 'normalized',    'Fscore': 93.20, 'Precision': 91.77, 'Recall': 94.67, 'description': "normalized:     Accented Greek Text (βίβλος)"},
    {'name': 'translit',      'Fscore': 91.71, 'Precision': 89.39, 'Recall': 94.14, 'description': "translit:       Transliteration, Non-Accented (Biblos)", "color": "gray"},
    {'name': 'norm+transl',   'Fscore': 92.74, 'Precision': 91.76, 'Recall': 93.73, 'description': "norm+transl:    Accented, Followed by Non-Accented (βίβλος_Biblos)", "color":"gray"},
    # {'name': 'norm<m>transl', 'Fscore': 92.66, 'Precision': 91.93, 'Recall': 93.40, 'description': "norm<m>transl:  Accented, Merged with Non-Accented (βBίiβbλlοoςs)", "color":"blue"},
    {'name': 'norm+lemma',    'Fscore': 93.53, 'Precision': 93.03, 'Recall': 94.03, 'description': "norm+lemma:     Normalized, followed by Lemma (γενέσεωςγένεσις)"},
    # {'name': 'nmt+llt',       'Fscore': 93.59, 'Precision': 93.02, 'Recall': 94.16, 'description': "nmt+llt:        norm<m>transl Followed by lemma<m>lemmatransl (ἐeγgέeνnνnηeσsεeνn_γgεeννnάaωo)", "color":"blue"},
    {'name': 'nlS',           'Fscore': 93.85, 'Precision': 93.05, 'Recall': 94.67, 'description': "nls:           norm+lemma signed, that is, each category is marked (נ:Βίβλοςל:βίβλος)", "color":"red"},
    # {'name': 'nmt+llt+cgp',   'Fscore': 94.20, 'Precision': 93.08, 'Recall': 95.34, 'description': "nmt+llt+cgp:    ... Followed by case, gender, person (ΒBίiβbλlοoςs_βbίiβbλlοoςs_nominative_feminine)", "color":"blue"},
    {'name': 'nlcgpS',        'Fscore': 94.55, 'Precision': 92.95, 'Recall': 96.21, 'description': "nlcgpS: norm + lemma + case + gender + person Signed (נ:Χριστοῦל:Χριστόςק:genג:mas)"},
    {'name': 'NLCM',          'Fscore': 94.63, 'Precision': 93.32, 'Recall': 95.97, 'description': "NLCM:           ... Followed by mood, sp, tense, morph (ἐeπpοoίiηeσsεeνn_πpοoιiέeωo_p_3_indicative_verbaoristV-AAI-3S)"},
    {'name': 'nlcgpnmst',     'Fscore': 95.17, 'Precision': 94.02, 'Recall': 96.35, 'description': "nlcgpnmst:      norm_lemma_case_gender_person_number_mood_sp_tense (🧭:ἐγέννησεν✂:γεννάωℕ:①⚙:●✎:→⏱:◆)"},
    {'name': 'IDEAL',         'Fscore': 100.00, 'Precision': 100.00, 'Recall': 100.00, 'description': ""}
]

# Generate the corresponding arrays for plotting
x1 = [item['name'] for item in data]
y1 = [item['Fscore'] for item in data]    # F-score
y2 = [item['Precision'] for item in data] # Precision
y3 = [item['Recall'] for item in data]      # Recall

fig, ax1 = plt.subplots()
ax1.grid(True, which="both", axis="both", linestyle="--", alpha=0.7)
plt.xticks(rotation=20, ha="right")   # 45° angle, aligned to the right

# Color the ticks based on each data's color property if it exists
for i, tick in enumerate(ax1.get_xticklabels()):
    if i < len(x1):
        for item in data:
            if x1[i] == item['name'] and 'color' in item:
                tick.set_color(item['color'])

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
    "A": -0.5,      # offset for F-Score
    "B": 0,         # offset for Precision
    "C": 0.75       # offset for Recall
}

for x, y in zip(x1, y1):
    ax1.text(x, y + offsets["A"], f"{y}", color="b", ha="center", va="bottom", fontsize=8)

for x, y in zip(x1, y2):
    ax2.text(x, y + offsets["B"], f"{y}", color="g", ha="center", va="bottom", fontsize=8)

for x, y in zip(x1, y3):
    ax3.text(x, y + offsets["C"], f"{y}", color="r", ha="center", va="bottom", fontsize=8)

description = "\n".join(item["description"] for item in data if item["description"])

plt.figtext(0.0, -0.1, description, wrap=True, ha="left", va="top", fontsize=9)
plt.show()
# %%

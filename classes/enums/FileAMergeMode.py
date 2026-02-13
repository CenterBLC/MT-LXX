from enum import Enum, auto

class FileAMergeMode(Enum):
    NORMALIZED = auto()  # Accented Greek Text (βίβλος)
    TRANSLIT = auto()  # Transliteration, Non-Accented (Biblos)
    NORM_TRANSLIT = auto()  # Accented, Followed by Non-Accented (βίβλος_Biblos)
    NORM_LEMMA = auto()  # Normalized, followed by Lemma (γενέσεωςγένεσις)
    NLS = auto()  # norm+lemma signed, that is, each category is marked (נ:Βίβλοςל:βίβλος)
    NLCGPS = auto()  # nlcgpS: norm + lemma + case + gender + person Signed (נ:Χριστοῦל:Χριστόςק:genג:mas)
    NLCM = auto()  # NLCM: ... Followed by mood, sp, tense, morph (ἐeπpοoίiηeσsεeνn_πpοoιiέeωo_p_3_indicative_verbaoristV-AAI-3S)
    NLCGPNMST = auto()  # nlcgpnmst: norm_lemma_case_gender_person_number_mood_sp_tense (🧭:ἐγέννησεν✂:γεννάωℕ:①⚙:●✎:→⏱:◆)
    
    def __str__(self) -> str:
        return self.name.title().lower()
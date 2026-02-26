# from classes.Manager import Manager
from .GntApiWrapper import GntApiWrapper
from .enums.FileAMergeMode import FileAMergeMode

from tf.core.nodefeature import NodeFeatures
from tf.core.locality import Locality

class FeatureMerger():
    def __init__(self, manager):
        # self._manager = manager
        self._fileA_merge_mode: FileAMergeMode = manager.settings.fileA_merge_mode
        self._gnt_wrapper: GntApiWrapper = manager.gnt_wrapper
    
    @property
    def F(self) -> NodeFeatures:
        return self._gnt_wrapper.F
    
    # @property
    # def L(self) -> Locality:
    #     return self._gnt_wrapper.L

    abbreviations = [ 
            {'feature':'case', 'nominative':'⊙', 'accusative':'◉', 'genitive':'∈', 'dative':'⇨', 'vocative': '📣'},
            {'feature':'gender', 'masculine':'♂', 'feminine':'♀', 'neutral':'⚲'},
            {'feature':'person', 'p1':'🧑', 'p2':'👤', 'p3':'👥'},
            {'feature':'number', 'singular':'①', 'plural':'∴'},

            {'feature':'mood', 'indicative':'●', 'infinitive':'∾', 'participle':'▦', 'subjunctive':'△', 'imperative':'⚡', 'optative':'☆', },
            {'feature':'sp', 'subs':'■', 'verb':'→', 'art':'▣', 'conj':'∧', 'pron':'☺', 'prep':'↦', 'adjv':'✦', 'advb':'⋆', 'intj':'‼', 'num':'№'},
            {'feature':'tense', 'aorist':'◆', 'present':'≈', 'imperfect':'◐', 'future':'⇢', 'perfect':'◎', 'pluperfect':'⨀'},   
        ]

    def get_word(self, word: str) -> str:

        match self._fileA_merge_mode:
            case FileAMergeMode.NLCGPNMST:
                return self.get_word_NLCGPNMST(word)
            case _:
                return None
        
        # region Previous Modes
        # used in case of one of the FileAMergeMode modes:
        # def merge_normalized_translit(api_f, word: str) -> str:
        #     s1 = api_f.normalized.v(word)
        #     s2 = api_f.translit.v(word)

        #     return FeatureMerger.merge_strings(s1, s2)
        
        # used in case of one of the FileAMergeMode modes:
        # def merge_lemma_lemmatranslit(api_f, word: str) -> str:
        #     s1 = api_f.lemma.v(word).replace(" ", "") # fix against error lemma's -- both have issues
        #     s2 = api_f.lemmatranslit.v(word).replace(" ", "") # fix against error lemmatranslit's -- both have issues

        #     return FeatureMerger.merge_strings(s1, s2)
        # endregion
    
    def get_feature_value(self
                            , api_feature: str
                            , feature_name: str
                            , feature_sign: str
                            , word: str) -> str:

        # api_f.case.v(word)
        value = api_feature.v(word) if hasattr(self.F, feature_name) else ''
        for abbr in self.abbreviations:
            if feature_name == abbr.get('feature'):
                if value in abbr:
                    value = abbr[value]
                break
        value = '' if value in (None, '') else f"{feature_sign}:{value.replace(' ', '')}"
        # value = '' if value in (None, '') else value[:5] # 2 characters are technical and 3 -- part of the value itself
        
        return value

    def retreive_case_gender_person_number(self, word: str) -> str:
        
        case_value = self.get_feature_value(self.F.case, 'case', '💼', word)
        gender_value = self.get_feature_value(self.F.gender, 'gender', '☼', word)
        person_value = self.get_feature_value(self.F.person, 'person', '🧍' ,word)
        number_value = self.get_feature_value(self.F.number, 'number', 'ℕ',word)

        return case_value + gender_value + person_value + number_value
    
    def retreive_mood_sp_tense(self, word: str) -> str:

        mood_value = self.get_feature_value(self.F.mood, 'mood', '⚙', word)
        sp_value = self.get_feature_value(self.F.sp, 'sp', '✎',  word)
        tense_value = self.get_feature_value(self.F.tense, 'tense', '⏱',  word)
        # morph_value = get_feature_value(api_f.morph, 'morph', word)

        return mood_value + sp_value + tense_value; # + morph_value

    # if lemma equals 'normalized', change it to samek (Hebrew letter) to save space
    def get_lemma_value(self, word: str, normalized: str) -> str:
        # this is a fix against lemma error with 'replace'; using Heberew 'lamed' character to tell AI that this is a separate 'lemma' entity value. ":" is a category separator for AI.
        value = self.F.lemma.v(word).replace(' ', '')
        value = '≡' if value == normalized else value
        return f"✂:{value}"

    def get_word_NLCGPNMST(self, word: str) -> str:
        
        # region preparing return blocks
        # using Heberew 'nun' character to tell AI that this is a separate 'normalized' entity value. ":" is a category separator for AI.
        normalized = self.F.normalized.v(word)
        n = f"🧭:{normalized}" 
        l = self.get_lemma_value(word, normalized)

        cgpn = self.retreive_case_gender_person_number(word)
        mst = self.retreive_mood_sp_tense(word) # morph is not needed as it repeats other features
        # endregion

        # res = nmt + llt + cgp + mstm
        res = n + l + cgpn + mst

        return res

    @staticmethod
    def merge_strings(s1: str, s2: str) -> str:
        # Pair characters from both strings
        result = []
        min_length = min(len(s1), len(s2))
        
        for i in range(min_length):
            # For even positions starting at 0, take from s1, then s2
            result.append(s1[i])
            result.append(s2[i])
        
        # Append the remaining part from the longer string if any
        if len(s1) > min_length:
            result.append(s1[min_length:])
        elif len(s2) > min_length:
            result.append(s2[min_length:])
        
        return ''.join(result)

        

    

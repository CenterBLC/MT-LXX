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

def merge_features(api_f, word: str) -> str:

    abbreviations = [ 
        {'feature':'case', 'nominative':'⊙', 'accusative':'◉', 'genitive':'∈', 'dative':'⇨', 'vocative': '📣'},
        {'feature':'gender', 'masculine':'♂', 'feminine':'♀', 'neutral':'⚲'},
        {'feature':'person', 'p1':'🧑', 'p2':'👤', 'p3':'👥'},
        {'feature':'number', 'singular':'①', 'plural':'∴'},

        {'feature':'mood', 'indicative':'●', 'infinitive':'∾', 'participle':'▦', 'subjunctive':'△', 'imperative':'⚡', 'optative':'☆', },
        {'feature':'sp', 'subs':'■', 'verb':'→', 'art':'▣', 'conj':'∧', 'pron':'☺', 'prep':'↦', 'adjv':'✦', 'advb':'⋆', 'intj':'‼', 'num':'№'},
        {'feature':'tense', 'aorist':'◆', 'present':'≈', 'imperfect':'◐', 'future':'⇢', 'perfect':'◎', 'pluperfect':'⨀'},
        
    ]
    
    def merge_normalized_translit(api_f, word: str) -> str:
        s1 = api_f.normalized.v(word)
        s2 = api_f.translit.v(word)

        return merge_strings(s1, s2)
    
    def merge_lemma_lemmatranslit(api_f, word: str) -> str:
        s1 = api_f.lemma.v(word).replace(" ", "") # fix against error lemma's -- both have issues
        s2 = api_f.lemmatranslit.v(word).replace(" ", "") # fix against error lemmatranslit's -- both have issues

        return merge_strings(s1, s2)
    
    # get_feature_value(, word: str) -> str:

    def get_feature_value(api_f, api_feature, feature_name, feature_sign, word: str) -> str:

        # api_f.case.v(word)
        value = api_feature.v(word) if hasattr(api_f, feature_name) else ''
        for abbr in abbreviations:
            if feature_name == abbr.get('feature'):
                if value in abbr:
                    value = abbr[value]
                break
        value = '' if value in (None, '') else f"{feature_sign}:{value.replace(' ', '')}"
        # value = '' if value in (None, '') else value[:5] # 2 characters are technical and 3 -- part of the value itself
        
        return value

    def retreive_case_gender_person_number(api_f, word: str) -> str:
        
        case_value = get_feature_value(api_f, api_f.case, 'case', '💼', word)
        gender_value = get_feature_value(api_f, api_f.gender, 'gender', '☼', word)
        person_value = get_feature_value(api_f, api_f.person, 'person', '🧍' ,word)
        person_value = get_feature_value(api_f, api_f.number, 'number', 'ℕ',word)

        return case_value + gender_value + person_value
    
    def retreive_mood_sp_tense(api_f, word: str) -> str:

        mood_value = get_feature_value(api_f, api_f.mood, 'mood', '⚙', word)
        sp_value = get_feature_value(api_f, api_f.sp, 'sp', '✎',  word)
        tense_value = get_feature_value(api_f, api_f.tense, 'tense', '⏱',  word)
        # morph_value = get_feature_value(api_f, api_f.morph, 'morph', word)

        return mood_value + sp_value + tense_value; # + morph_value

    # if lemma equals 'normalized', change it to samek (Hebrew letter) to save space
    def get_lemma_value(api_f, word: str, normalized: str) -> str:
        # fix against lemma error with 'replace'; using Heberew 'lamed' character to tell AI that this is a separate 'lemma' entity value. ":" is a category separator for AI.
        value = api_f.lemma.v(word).replace(' ', '')
        value = '≡' if value == normalized else value
        return f"✂:{value}"

    # region preparing return blocks
    # using Heberew 'nun' character to tell AI that this is a separate 'normalized' entity value. ":" is a category separator for AI.
    normalized = api_f.normalized.v(word)
    n = f"🧭:{normalized}" 
    l = get_lemma_value(api_f, word, normalized)

    cgpn = retreive_case_gender_person_number(api_f, word)
    mst = retreive_mood_sp_tense(api_f, word) # morph is not needed as it repeats other features
    # endregion

    # res = nmt + llt + cgp + mstm
    res = n + l + cgpn + mst

    return res

    

# if __name__ == "__main__":
#     print(merge_strings('γενέσεως', 'geneseos1234556789'))

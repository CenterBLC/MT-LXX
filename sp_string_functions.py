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

    def merge_normalized_translit(api_f, word: str) -> str:
        s1 = api_f.normalized.v(word)
        s2 = api_f.translit.v(word)

        return merge_strings(s1, s2)
    
    def merge_lemma_lemmatranslit(api_f, word: str) -> str:
        s1 = api_f.lemma.v(word).replace(" ", "") # fix against error lemma's -- both have issues
        s2 = api_f.lemmatranslit.v(word).replace(" ", "") # fix against error lemmatranslit's -- both have issues

        return merge_strings(s1, s2)
    
    # get_feature_value(, word: str) -> str:

    def get_feature_value(api_f, api_feature, feature_name, word: str) -> str:

        # api_f.case.v(word)
        value = api_feature.v(word) if hasattr(api_f, feature_name) else ''
        value = '' if value is None else value.replace(" ", "")
        return value

    def retreive_case_gender_person(api_f, word: str) -> str:
        
        case_value = get_feature_value(api_f, api_f.case, 'case', word)
        gender_value = get_feature_value(api_f, api_f.gender, 'gender', word)
        person_value = get_feature_value(api_f, api_f.person, 'person', word)

        return case_value + gender_value + person_value
    
    def retreive_mood_sp_tense_morph(api_f, word: str) -> str:

        mood_value = get_feature_value(api_f, api_f.mood, 'mood', word)
        sp_value = get_feature_value(api_f, api_f.sp, 'sp', word)
        tense_value = get_feature_value(api_f, api_f.tense, 'tense', word)
        morph_value = get_feature_value(api_f, api_f.morph, 'morph', word)

        return mood_value + sp_value + tense_value + morph_value

    nmt = merge_normalized_translit(api_f, word)
    llt = merge_lemma_lemmatranslit(api_f, word)
    cgp = retreive_case_gender_person(api_f, word)
    mstm = retreive_mood_sp_tense_morph(api_f, word)
    res = nmt + llt + cgp + mstm

    return res

    

# if __name__ == "__main__":
#     print(merge_strings('γενέσεως', 'geneseos1234556789'))
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

    # the list of possible features for addition
    # mood
    # sp
    # tense
    # morph

    def merge_normalized_translit(api_f, word: str) -> str:
        s1 = api_f.normalized.v(word)
        s2 = api_f.translit.v(word)

        return merge_strings(s1, s2)
    
    def merge_lemma_lemmatranslit(api_f, word: str) -> str:
        s1 = api_f.lemma.v(word).replace(" ", "") # fix against error lemma's -- both have issues
        s2 = api_f.lemmatranslit.v(word).replace(" ", "") # fix against error lemmatranslit's -- both have issues

        return merge_strings(s1, s2)

    def retreive_case_gender_person(api_f, word: str) -> str:
        # Retrieve case, gender, and person features from api_f for the given word.
        # Fallback to empty strings if any feature is missing.
        case_value = api_f.case.v(word) if hasattr(api_f, 'case') else ''
        gender_value = api_f.gender.v(word) if hasattr(api_f, 'gender') else ''
        person_value = api_f.person.v(word) if hasattr(api_f, 'person') else ''

        # Optional: Remove any spaces (in case the features include them)
        case_value = '' if case_value is None else case_value.replace(" ", "")
        gender_value = '' if gender_value is None else gender_value.replace(" ", "")
        person_value = '' if person_value is None else person_value.replace(" ", "")

        # Combine the features. Adjust the merging logic if needed.
        return case_value + gender_value + person_value

    
    nmt = merge_normalized_translit(api_f, word)
    llt = merge_lemma_lemmatranslit(api_f, word)
    cgp = retreive_case_gender_person(api_f, word)
    res = nmt + llt + cgp

    return res

    

# if __name__ == "__main__":
#     print(merge_strings('γενέσεως', 'geneseos1234556789'))
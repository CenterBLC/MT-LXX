def merge_strings(from_str: str, s1: str, s2: str) -> str:
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
    
    return from_str.join(result)



def merge_features(api_f, word: str) -> str:

    # the list of possible features for addition
    # lemma
    # lemmatranslit
    # case
    # gender
    # person
    # mood
    # sp
    # tense
    # morph

    def merge_normalized_translit(from_str, api_f, word: str) -> str:
        s1 = api_f.normalized.v(word)
        s2 = api_f.translit.v(word)

        return merge_strings(from_str, s1, s2)
    
    def merge_lemma_lemmatranslit(from_str, api_f, word):
        s1 = api_f.lemma.v(word).replace(" ", "") # fix against error lemma's -- both have issues
        s2 = api_f.lemmatranslit.v(word).replace(" ", "") # fix against error lemmatranslit's -- both have issues

        return merge_strings(from_str, s1, s2)
    
    nmt = merge_normalized_translit('', api_f, word)
    llt = merge_lemma_lemmatranslit('',  api_f, word)
    res = nmt + llt

    return res

    

if __name__ == "__main__":
    print(merge_strings('γενέσεως', 'geneseos1234556789'))
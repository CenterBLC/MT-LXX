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

if __name__ == "__main__":
    print(merge_strings('γενέσεως', 'geneseos1234556789'))

class StringMerger:
    """
    A utility class for merging two strings by interleaving their characters.
    This class takes two input strings and combines them by alternating characters
    from each string until one string is exhausted, then appends any remaining
    characters from the longer string.
    Attributes:
        s1 (str): The first string to merge.
        s2 (str): The second string to merge.
    """
    def __init__(self, s1: str, s2: str) -> None:
        """
        Initialize the StringMerger with two strings.
        Args:
            s1 (str): The first string to merge.
            s2 (str): The second string to merge.
        """
        """
        Merge two strings by interleaving their characters.
        Pairs characters alternately from both input strings starting from index 0.
        Once one string is exhausted, appends any remaining characters from the
        longer string to the result.
        Returns:
            str: A merged string with interleaved characters from s1 and s2.
        Example:
            >>> merger = StringMerger("abc", "xyz")
            >>> merger.merge_strings()
            'axbycz'
        """
        self.s1 = s1
        self.s2 = s2

    def merge_strings(self) -> str:
        # Pair characters from both strings
        result = []
        min_length = min(len(self.s1), len(self.s2))
        
        for i in range(min_length):
            # For even positions starting at 0, take from s1, then s2
            result.append(self.s1[i])
            result.append(self.s2[i])
        
        # Append the remaining part from the longer string if any
        if len(self.s1) > min_length:
            result.append(self.s1[min_length:])
        elif len(self.s2) > min_length:
            result.append(self.s2[min_length:])
        
        return ''.join(result)
"""
Checks a pattern string against a comparison string.\n
Case insensitive, strict length comparison only.\n
In case of an error, either one of two things happens: either a word mismatches on the pattern, or the pattern mismatches on the word.

>>> pattern = 'aabbc'
>>> str1 = 'meow meow woof woof oink' #// True
>>> str2 = 'meow woof oink oink oink' #// False
"""


pattern1 = "aabac"
str1 = "woof woof meow woof oink"

pattern2 = "ab"
str2 = "hey hey"

pattern3 = "aa"
str3 = "hey bye"

pattern4 = "aa"
str4 = "hey hey hey"

pattern5 = "aaa"
str5 = "hey hey"


# Case insensitive, strict length comparison
def pattern_match(pattern:str, string:str) -> bool:
    """Takes a pattern string and input string,
    compares pattern against input
    and returns appropriate boolean on match."""

    print(pattern,"<>",string)

    string_split = string.lower().split(" ")
    pattern_split = [*pattern.lower()]
    assigned = {}

    if len(string_split) != len(pattern_split):
        print("Pattern and string must have the same length")
        return False

    for i, (pat, word) in enumerate(zip(pattern_split,string_split)):

        if word not in assigned and pat not in assigned.values():
            assigned[word] = pat
            print(f"{i} | '{word}:{pat}' added to assigned dict")
        else:

            try:
                if (assigned[word] != pat): # The KeyError takes place in assigned[word]
                    print(f"x | No match, {word}={pat} found, {word}={assigned[word]} expected\n")
                    return False
            except KeyError:
                print(f"x | No match, tried '{word}={pat}' but '{pat}' has already been assigned\n")
                return False

            print(f"{i} | '{word}:{pat}' Pattern compliant")

    print("v | Pattern match\n")
    return True


pattern_match(pattern1, str1)
pattern_match(pattern2, str2)
pattern_match(pattern3, str3)
pattern_match(pattern4, str4)
pattern_match(pattern5, str5)

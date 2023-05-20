"""
This function finds the longest substring with no repeating characters.
It uses a sliding window approach to read the string and returns the largest window it can.
I tried to keep corner-case catching to a minimum to preserve code clarity.
"""


string1 = "arsuijfkasdik"
string2 = "asgegregesarysagefhaesgrknelo"


def longest_sub(strng):
    '''
    >>> longest_sub("Hello World!")
    >>> "lo W"
    '''

    print()

    if not isinstance(strng, str) or not strng:
        print("Invalid input, input must be a 0+ length string")
        return False

    search = [*strng]
    last = len(strng)

    start, end = 0, 0 # Dynamic window (looks for largest)
    s, e = 0, 0 # Static window (largest found)

    while end < last:
        if search[end] not in search[start:end]:
            end += 1
        else:
            if (end-start) > (e-s):
                s, e = start, end
            start += search[start:end].index(search[end]) + 1

    if s + e == 0 and start + end != 0:
        print(f'Largest substring without repeating characters is the entire string\n"{strng}"')
        return strng

    longest_substring = "".join(search[s:e])

    print('The longest substring in:')
    print(f'"{strng}"')
    print(f'is "{longest_substring}", from letter number {s+1} to number {e}.')

    return longest_substring


longest_sub("Hello, World!")
longest_sub("Foo bar baz")
longest_sub(string1)
longest_sub(string2)
longest_sub("abcdefg")
longest_sub('')

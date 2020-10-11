import sys
sys.setrecursionlimit(10000)


def consume_regex(word1, word2):
    if len(word2) < len(word1):
        return False
    char_1 = word1[0]
    char_2 = word2[0]
    is_match = char_1 == "." or char_1 == char_2
    if len(word1) == 1:
        return is_match
    else:
        if is_match:
            return consume_regex(word1[1:], word2[1:]) or consume_regex(word1, word2[1:])
        else:
            return consume_regex(word1, word2[1:])


string = input()
if string == "":
    print(False)
else:
    words = string.split("|")
    if words[0] == "":
        print(True)
    elif words[1] == "":
        print(False)
    else:
        print(consume_regex(words[0], words[1]))

import sys
sys.setrecursionlimit(10000)
reg_st = False
reg_end = False


def reg_metachar(word1, word2, is_slice):
    if word1[1] == "?":
        return consume_regex(word1[0] + word1[2:], word2, is_slice) or consume_regex(word1[2:], word2, is_slice)
    if word1[1] == "+":
        return (word1[0] == "." or word1[0] == word2[0]) and (consume_regex(word1[2:], word2[1:], is_slice) or consume_regex(word1, word2[1:], is_slice))
    if word1[1] == "*":
        return (consume_regex(word1[2:], word2, is_slice)) or ((word1[0] == "." or word1[0] == word2[0]) and (consume_regex(word1[2:], word2[1:], is_slice) or consume_regex(word1, word2[1:], is_slice)))


def consume_regex(word1, word2, is_slice):
    if word1 == "":
        return reg_st or word2 == "" or not reg_end
    if word2 == "":
        return False
    is_match = word1[0] == "." or word1[0] == word2[0]
    if word1[0] == "\\":
        if word1.startswith("\\."):
            is_match = word1[1] == word2[0]
        else:
            is_match = word1[1] == "." or word1[1] == word2[0]
        word1 = word1[1:]
    if len(word1) == 1:
        if reg_end:
            return (len(word2) == 1 and is_match) or (not reg_st and is_slice and consume_regex(word1, word2[1:], is_slice))
        elif reg_st:
            return is_match
        else:
            return is_match or (is_slice and consume_regex(word1, word2[1:], is_slice))
    if word1[1] in "?*+":
        return reg_metachar(word1, word2, is_slice)
    if reg_st:
        return is_match and consume_regex(word1[1:], word2[1:], False)
    return (is_match and consume_regex(word1[1:], word2[1:], False)) or (is_slice and consume_regex(word1, word2[1:], is_slice))


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
        reg_st = words[0].startswith("^")
        reg_end = words[0].endswith("$") and not words[0].endswith("\\$")
        if reg_st:
            words[0] = words[0][1:]
        if reg_end:
            words[0] = words[0][:-1]
        print(consume_regex(words[0], words[1], True))

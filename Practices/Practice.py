def long_word(word : str) ->bool:
    is_long = len(word)
    if is_long >= 7:
        return True
    else:
        return False
print(long_word("Mauricio"))

def first_longer_than_second(word1 : str, word2 : str):
    len_word1 = len(word1)
    len_word2 = len(word2)
    if len_word1 >  len_word2:
        return True
    elif len_word1 <  len_word2:
        return False
    else:
        return "Son Iguales"

print(first_longer_than_second("Puto","gayo"))


def long_word2(word : str) ->bool:
    return len(word) > 7
print(long_word2("Mauricio"))


def first_longer_than_second2(word1 : str, word2 : str) -> bool:
    return len(word1) > len(word2)
print(first_longer_than_second("Puto","gay"))

def same_first_and_last_letter(word):
    return word[0] == word[-1]
print( "es", same_first_and_last_letter("OllO"))


def three_number_sum(word):
    return int(word[0]) + int(word[1]) + int(word[2])
print(three_number_sum("444"))
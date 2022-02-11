def rep_word(sentence1, sentence2=''):
    sentence1 = sentence1.split()
    sentence2 = sentence2.split()
    d = {i: (sentence1 + sentence2).count(i) for i in (sentence1 + sentence2)}
    m_value = max(d.values())
    if m_value == 1:
        return "There are no common words"
    else:
        word = [word for word in d.keys() if d[word] == m_value]
    return word[len(word) - 1]


st1 = input('Enter a sentence: ')
st2 = input('Enter a second sentence: ')
print(rep_word(st1, st2))

sentence = input('Type a sentence:')
sym_to_find = input('Type a symbol for replacement in your sentence:')
ind = sentence.find(sym_to_find)
if ind == -1:
       print('There are no such symbols in your sentence!')
else:
    new_sentence = sentence[0] + sentence[1: len(sentence)-1].replace(sym_to_find, sym_to_find.upper()) + sentence[len(sentence)-1]
    print(new_sentence)
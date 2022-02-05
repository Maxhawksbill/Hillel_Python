sentence = input('Type a sentence:')
sym_to_find = input('Type a symbol for replacement in your sentence:')
ind = sentence.find(sym_to_find)
ind_first = sentence.find(sym_to_find)
shift_ind = sentence.find(sym_to_find)
if ind == -1:
       print('There are no such symbols in your sentence!')
else:
    while ind != -1:
        ind = sentence.find(sym_to_find, shift_ind)
        if ind == -1:
            break
        shift_ind = ind + 1
    new_sentence = sentence[0: ind_first + 1] + sentence[ind_first + 1: shift_ind - 1].replace(sym_to_find, sym_to_find.upper())\
               + sentence[shift_ind - 1: len(sentence)]
    print(new_sentence)
sentence = input('Type a sentence:')
sym_to_find = input('Type a symbol to find in your sentence:')
ind = sentence.find(sym_to_find)
if ind == -1:
       print('There are no such symbols in your sentence!')
else:
    t = 0
    shift_ind = 0
    while ind != -1:
        ind = sentence.find(sym_to_find, shift_ind)
        if ind == -1:
             break
        shift_ind = ind + 1
        t = t + 1
    print('Your symbol -' + sym_to_find + '- was found ' + str(t) + ' time (s)')
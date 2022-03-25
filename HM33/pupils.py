from pprint import pprint as pp

lst = []
file = open('src_14.txt', 'rt', encoding='utf-8')
while True:
    line = file.readline()
    if line != '':
        lst.append(line.strip('\n').split())
    else:
        break
file.close()
summ_total = 0
avrg_total = 0
lst1 = []
for row in lst:
    summ = 0
    avrg = 0
    t = 0
    for i in range(0, len(row)):
        if not row[i].isnumeric():
            continue
        t += 1
        summ += int(row[i])
    avrg = round(summ / t, 2)
    row.append(str(avrg))
    summ_total += summ
    if avrg < 5:
        lst1.append(" ".join(row))
avrg_total = round(summ_total / (len(lst)*t), 2)
print("Pupils which have average mark less than 5, are:")
pp(lst1)
print(f'Average mark in class: {avrg_total}')
file1 = open('example_file.txt', 'w', encoding='utf-8')
for line in lst:
    file1.writelines(str(line[1] + ' ' + line[0][0] + '.').ljust(20))
    file1.writelines('\t')
    file1.writelines(line[len(line) - 1].rjust(5))
    file1.write('\n')
file1.close()



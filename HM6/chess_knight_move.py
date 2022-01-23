chess_letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
chess_numbers = ["1", "2", "3", "4", "5", "6", "7", "8"]
print('  a b c d e f g h\n'
      '8|_|_|_|_|_|_|_|_|8\n'
      '7|_|_|_|_|_|_|_|_|7\n'
      '6|_|_|_|_|_|_|_|_|6\n'
      '5|_|_|_|_|_|_|_|_|5\n'
      '4|_|_|_|_|_|_|_|_|4\n'
      '3|_|_|_|_|_|_|_|_|3\n'
      '2|_|_|_|_|_|_|_|_|2\n'
      '1|_|_|_|_|_|_|_|_|1\n'
      '  a b c d e f g h')
cell1 = input('Choose any two cells from the ChessBoard above!\n'
              'In the format of a combination of a Letter and a Number (i.e., a1, h7, etc.)\n'
              'And the program will check if a Knight can step from cell#1 to the cell#2\n'
              'Enter a first cell:')
cell2 = input('Enter a second cell:')
while cell1[0:1] not in chess_letters or cell1[1:2] not in chess_numbers or \
        cell2[0:1] not in chess_letters or cell2[1:2] not in chess_numbers:
    cell1 = input('Cells you have entered DO NOT belong to the ChessBoard!\n'
                  'Try again!\n'
                  'Enter first point:')
    cell2 = input('Enter second point:')
    if cell1[0:1] not in chess_letters or cell1[1:2] not in chess_numbers or \
            cell2[0:1] not in chess_letters or cell2[1:2] not in chess_numbers:
        continue
    else:
        break
cell1_letter = chess_letters.index(cell1[0:1])
cell1_number = chess_numbers.index(cell1[1:2])
cell2_letter = chess_letters.index(cell2[0:1])
cell2_number = chess_numbers.index(cell2[1:2])
#print(cell1_letter, type(cell2_letter), cell1_number, cell2_letter, cell2_number)
if (abs(cell1_letter - cell2_letter) == 2) and (abs(cell1_number - cell2_number) == 1) or \
    (abs(cell1_letter - cell2_letter) == 1) and (abs(cell1_number - cell2_number) == 2):
    print('Knight can be moved to the cell#2')
else:
    print('Knight can not be moved to the cell#2')
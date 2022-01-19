schoolmate_qty = input('Type quantity of schoolmates:')
apple_qty = input('Type quantity of apples:')
if int(schoolmate_qty) == 0:
    print('You do not have schoolmates to share with!')
elif int(schoolmate_qty) > int(apple_qty):
    print('Apples will be enough for:\t'+ apple_qty + ' schoolmate(s)')
else:
    sm_apple = int(apple_qty) / int(schoolmate_qty)
    apple_left = int(apple_qty) % int(schoolmate_qty)
    print('Each schoolmate receive:\t' + str(int(sm_apple)) + ' apple(s)')
    print('Apples left in a bucket:\t' + str(int(apple_left)))
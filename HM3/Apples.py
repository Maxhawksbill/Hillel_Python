schoolmate_qty = input('Type quantity of schoolmates:')
apple_qty = input('Type quantity of apples:')
schoolmate_qty = int(schoolmate_qty)
apple_qty = int(apple_qty)
if schoolmate_qty == 0:
    print('You do not have schoolmates to share with!')
elif (schoolmate_qty > apple_qty) or apple_qty == 0:
    print('Apples will be enough ONLY for:\t' + str(apple_qty) + ' schoolmate(s) out of ' + str(schoolmate_qty))
else:
    sm_apple = apple_qty // schoolmate_qty
    apple_left = apple_qty % schoolmate_qty
    print('Each schoolmate receive:\t' + str(sm_apple) + ' apple(s)')
    print('Apples left in a bucket:\t' + str(apple_left))
book = [[34587, 'Learning Python, Mark Lutz', 4, 40.95],
        [98762, 'Programming Python, Mark Lutz', 5, 56.80],
        [77226, 'Head First Python, Paul Barry', 3, 32.95],
        [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]]

order = list(zip(list(map(lambda order_no: order_no[0], book)),
                 list(map(lambda ammount: round((ammount[2] * ammount[3]), 2) if ammount[2] * ammount[
                     3] > 100 else round((ammount[2] * ammount[3] + 10), 2), book))))
print(order)


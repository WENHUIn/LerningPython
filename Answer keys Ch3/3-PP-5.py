## Compare IRA balances when starting early vs. starting late.
earl = 0
larry = 0
for year in range(15):
    # first 15 years between 2015-2063
    earl = 1.04 * earl + 5000
for year in range(33):
    # remaining 33 years between 2015-2063
    larry = 1.04 * larry + 5000
    earl *= 1.04
earlDeposited = 15 * 5000
larryDeposited = 33 * 5000
print("AMOUNTS DEPOSITED".center(45))
print("Earl: ${:<10,.2f}\t    Larry: ${:10,.2f}"
      .format(earlDeposited, larryDeposited))
print("AMOUNTS IN IRA UPON RETIREMENT".center(45))
print("Earl: ${:10,.2f}\t    Larry: ${:10,.2f}".format(earl, larry))

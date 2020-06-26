## Depreciation of an automobile.
value = 20000
##print("{0}     ${1:7,.2f}".format(0, value))
for i in range(1, 5):
    value = .85 * value
    print("{0}     ${1:7,.2f}".format(i, value))
   

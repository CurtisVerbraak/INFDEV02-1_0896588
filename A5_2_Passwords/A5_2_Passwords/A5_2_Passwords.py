## passwords

input = raw_input("Enter a password\n")
length = len(input)

lc = sum(1 for a in input if a.islower())
uc = sum(1 for a in input if a.isupper())
no = sum(1 for a in input if a.isdigit())

if lc > 2 and uc > 2 and no > 2 and length > 10:
    print ('Password is strong')
elif lc > 1 and uc > 1 or no > 1 and length > 6:
    print ('Password is medium strong, try more numbers and uppercases')
elif length < 5:
    print('you sure you want a password that small!?')
else:
    print ('password is weak')
## passwords

inupt = raw_input("Enter a password\n")
var = ""
for i in range(len(inupt),0,-1):
    var += inupt[i-1]
print (var)
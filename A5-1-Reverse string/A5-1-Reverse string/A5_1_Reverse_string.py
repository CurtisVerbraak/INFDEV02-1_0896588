## reverse string
inupt = raw_input("type something useless and press enter!\n")

var = ""
for i in range(len(inupt),0,-1):
    var += inupt[i-1]
print (var)
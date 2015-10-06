## SQuare triangle circle

#Square
width = 5
for i in range(0,5):
    print("*" * width)

#hollow square
print ("\n \n")

x = "*"
t = " "

for i in range(0,5):
    if i == 0 or i == 4:
        var = x * 5
    else:
        var = x + t * 4 + x
    for j in range(0,1):
        print(var)

#triangle
for i in range(0,5):
    var = x * i 
    for j in range(0,1):
        print(var)

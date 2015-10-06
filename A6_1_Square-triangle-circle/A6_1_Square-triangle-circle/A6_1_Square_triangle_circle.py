## SQuare triangle circle

#Square
width = 5
for i in range(0,5):
    print("*" * width)


##---------------------
print ("\n \n")
##---------------------

#hollow square
x = "*"
t = " "

for i in range(0,4):
    if i == 0 or i == 3:
        var = x * 5
    else:
        var = x + t * 3 + x
    for j in range(0,1):
        print(var)

#triangle
for i in range(0,5):
    var = x * i 
    for j in range(0,1):
        print(var)

##--------------------- 
print ("\n \n")
##---------------------

#piramide
for i in range(0,5,-1):

    for j in range(0,1):
        print(var)
#Square
size = raw_input('enter size in numbers for a square \n')
size = int(size)

for i in range(size):
    for j in range(size):
        if (j < size-1):
            var = "*"
        else:
            var = "*""\n"
        print (var),
     
##---------------------
print ("\n \n")
##---------------------

#hollow square
x = "*"
t = " "
size = raw_input('enter size in numbers for a hollow square \n')
size = int(size)
for i in range(0,size,1):
    if i == 0 or i == size-1:
       var = ""
       for j in range(size):
           var += x
    else:
        for j in range(size):
           # positie 1 en eind bezet
           var = x
           # omdat 1 en eind bezet zijn maak ik de size -2 
           # (size = 10) 1 en 10 zijn bezet, size-2 om de tussen characters te vullen (8+ begin char en eind char maakt 10)
           for j in range(size-2):
                var += t
           var += x
    print(var) 
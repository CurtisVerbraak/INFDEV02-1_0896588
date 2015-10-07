## Curtis Verbraak 0896588
## SQuare triangle circle

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
        # int (size-2) voor een beter resultaat, int gebruiken om str/int te onderscheiden
        var = x + t * int(size-2) + x
    for j in range(0,1,1):
        print(var)


#triangle
size = raw_input('enter size in numbers for a triangle \n')
size = int(size)
#size +1 om het aantal regels te printen welk bij input wordt aangegeven
for i in range(1,size+1,1):
    var = ""
    for j in range(1,i,1):
        var += "*"
    for j in range(0,1,1):
        print(var)

##--------------------- 
print ("\n \n")
##---------------------

#piramide
size = raw_input('enter size in numbers 3 to 20 for a triangle \n')

size = int(size)
if(size > 3 and size < 21):
    var = ''
    for i in range(0,size,1):
        for j in range(1,size-i,1):
            var += ' '
        for j in range(0,1+(i+i),1):
            var += '*'
        var += '\n'
 
    print (var)

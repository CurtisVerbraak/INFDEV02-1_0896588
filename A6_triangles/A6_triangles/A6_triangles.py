#triangle
size = raw_input('enter size in numbers for a triangle \n')
size = int(size)+1
x = "*"
#size +1 om het aantal regels te printen welk bij input wordt aangegeven
for i in range(0,size,1):
    var = ""
    for j in range(0,i,1):
        var += x
    print(var)

##--------------------- 
print ("\n \n")
##---------------------

#piramide
size = raw_input('enter size in numbers 3 to 20 for a triangle \n')
size = int(size)
x = "*"
t = " "
print size
if(size > 3 and size < 21):
    var = ""
    for i in range(0,size,1):
        for j in range(1,size-i,1):
            var += t
            print "t = x",
            print size-i
        for j in range(0,1+(i+i),1):
            var += x
            print "* = x",
            print 1+(i+i)
        var += '\n'
    
    print (var)
    #--------------------1------------------
##def printMax (a,b):
##    if(a > b):
##        print(a , "is maximum")
##    elif(a == b):
##        print(a , "is equal ")
##    else:
##        print(b , "is maximum")
##
##printMax(3,4)     ## 4 is maximum

#---------------------2----------------
##
##def power(x , y=2):
##    r = 1;
##    for i in range(y):
##        r = r * x;
##        return r;
##print(power(3));
##print(power(3,3))


##
##a = 10;
##b = 20;
##
##def change():
##    global b
##    a = 46
##    b = 56
##change()
##print(a)
##print(b)

def a(b):
    b = b + [5,3]
c = [1]
a(c)
print(len(c))

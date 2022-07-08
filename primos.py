num=int(input("Ingrese un número: "))

primo=False

for x in range(num,0,-1):
    if(x!=num):
        if(x!=1):
            if(num%x)==0:
                primo=False
                break
            else:
                primo=True

if primo:
    print(str(num)+ ' Es un número primo')
else:
    print(str(num)+ ' Es un número complejo')
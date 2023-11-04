print("WELCOME!!!This program helps you to print various patterns!")
print("The options for pattern printing are:")
print("(1)Left aligned Right angled Triangle.")
print("(2)Right aligned Right angled Triangle.")
print("(3)Center aligned triangle.")
print("(4)A Square.")


while True:
    ask=int(input("What do you want to do?(1/2/3/4)"))
    sym=input("Enter symbol/word/number for the pattern:")
    i1=int(input("Enter number of rows for your pattern:"))
    if (ask==1):
        for a in range(0,i1+1):
            for b in range(1,i1+2):
                if(b<=a):
                    print(sym,end=' ')
            print('\r')


    if (ask==2):
        
        c=2*i1-2
        for a in range(0,i1):
            for b in range(0,c):
                print(end=' ')
            for b in range(0,i1+1):
                if(b<=a):
                    print(sym,end=' ')
            print("\r")
            
            """
        for j in range (ask):
            print((sym) * (j + 1))
"""

    if (ask==3):
        for i in range(0,i1):
            for j in range(0,i1+1):
                if(j>=i1-i and j<=i1+i):
                    print(sym, end=" ")
                else:
                    print(" ",end='')
        print() 


    if (ask==4):
        for a in range(0,i1):
            for b in range(0,i1):
                print(sym,end=' ')
            print('\r')


    ch=input("Do you want to continue?(yes/no)")
    if(ch=="no"):
        print("BYEEE!!!")
        break

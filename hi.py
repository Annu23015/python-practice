## print first 10 number using while loop
##i=1
##while i<=10:
##    print(i)
##    i=i+1
##    

##***********************************************************************************************************************
##print the pattern
##1
##22
##333
##4444
##n=int(input("enter a number"))
##for i in range(1,n+1):
##    for j in range(1,n+1):
##        if i>=j:
##            print(i,end="")
##    print()
##**********************************************************************************************************************
##print pettern 
##1
##12
##123
##1234
##12345
##n=int(input("enter a number"))
##for i in range(1,n+1):
##    for j in range(1,i+1):
##        print(j,end="")
##    print("")
##************************************************
##n=int(input("enter a number"))    
##for i in range(1,n+1):
##    for j in range(1,n+1):
##        if i>=j:
##            print(j,end="")
##    print()

##************************************************************************************************************
##n=int(input("enter a number"))
##s=0
##while n>=0:
##    s=s+n
##    n=n-1
##print(s)    
    
##*****************************************************************************************************************
####display numbers from a list using loop
##con-1->The number must be divisible by five
##con-1->If the number is greater than 150, then skip it and move to the next number
##con-1->If the number is greater than 500, then stop the loop
##n=int(input("enter a number"))
##l=[]
##n=int(input("enter a number"))
##for j in range(1,n+1):
##    e=int(input("enter the list element"))
##    l.append(e)
##for i in l:
##    if i>500:
##        break
##    elif i>150:
##        continue
##    elif i%5==0:
##        print(i)    

##*********************************************************************************

####count the total number of digit in a number
##n=int(input("enter a number"))
##count=0
##while n!=0:
##    d=n%10
##    count=count+1
##    n=n//10
##print(count)
##
##*********************************************
##n=int(input("enter a number"))
##count=0
##while n!=0:
##    n=n//10
##    count=count+1
##print(count)

##***************************************************************************************************************************

####print the following pattern
##54321
##4321
##321
##21
##1
##n=int(input("enter a number"))
##for i in range(n,0,-1):
##    for j in range(n,0,-1):
##        if i>=j:
##            print(j,end=" ")
##    print()        
##*************************************************************************************************************

##print a list in reverse order using loop

##l=[11,22,33,44,55]
##n_l=reversed(l)
##for i in n_l:
##    print(i)
##***********************************************    
##l=[]
##n=int(input("enter a number"))
##for i in range(n):
##    e=int(input("enter the list element"))
##    l.append(e)
##l1=reversed(l)
##for j in l1:
##    print(j)

##*****************************************************************************************************************
##print all the number -10 to -1 using for loop

##for i in range(-10,0,1):
##    print(i)

##******************************************************************************************************************

##for i in range(5):
##    print(i)
##else:
##    print("done!")
##**************************************************************************************************************************
##Write a program to display all prime numbers within a range
##l_num,u_num=map(eval,input("enter lower number and upper number").split())
##for i in range(l_num,u_num):
##    if i>1:
##        for j in range(2,i//2):
##            if i%j==0:
##                break
##        else:
##            print(i)
    
##*****************************************************************************************************************        
        
## Reverse a given integer number

##n=int(input("enter the number"))
##while n>0:
##    r=n%10
##    print(r,end="")  or re=(re*10)+r
##    n=n//10
                          ##print(re)    

##***************************************************************************************************************************

##Use a loop to display elements from a given list present at odd index positions

##li=[10,20,30,40,50,60,70,80,90,100]
####p=len(li)
####
####for i in range(1,p,2):
####    print(li[i])
##
##for i in li[1::2]:
##    print(i)








































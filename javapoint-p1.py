#### find the area of trangle
####l=int(input("enter the length of triangle"))
####b=int(input("enter the breath of triangle"))
####area=(l*b)//2
####print("area=",area)
##
####*******************************************************************************************************************
##
####import cmath
###### to solve the quadratric equation
####
####
####a=float(input("enter the value of a"))
####b=float(input("enter the value of b"))
####c=float(input("enter the value of c"))
####
####d=(b**2)-(4*a*c)
####sol1=(-b-(cmath.sqrt(d)))/(2*a)
####sol2=(-b+(cmath.sqrt(d)))/(2*a)
####print("the solution is {} and {}".format(sol1,sol2))
##
##
####************************************************************************************************************
####import random
####n=int(input("enter a number"))
####a=[]
####for i in range(1,n):
####    p=random.randint(1,50)
####    a.append(p)
####print(a)
##
##
####**********************************************************************************************************************
##
##
####display the calender
####import calendar
####mm=int(input("enter the month"))
####yy=int(input("enter the year"))
####print(calendar.month(yy,mm))
##
##
##
####******************************************************************************************************************************
##
####convert km into miles
####kilometer=int(input("enter a number"))
####mi=0.6213711922
####miles=kilometer*mi
####print("km in mile",miles)
##
##
####***************************************************************************************************************************************************
##
####convert celsius into fahrenheit
####cel=float(input("enter the degree in celsius"))
####fahranheit=(cel*1.8)+32
####print("the %.2f dgree celsius is equal to %.2f fahrenheit"%(cel,fahranheit)) 
##
##
####**********************************************************************************************************************************************************
##
####yr=int(input("enter the year"))
####if yr%400==0 or yr%100!=0 and yr%4==0:
####    print("leap year")
####else:
####    print("not leap year")
##    
####****************************************************************************************
##
####a,b=10,20
####a,b=b,a
####print("a=",a)
####print("b=",b)
####*****************************************************************************************************
####n=int(input("enter a number"))
####if n>1:
####    for i in range(2,int(n/2)+1):
####        if n/i:
####            print(n,"not a prime number")
####            break
####    else:
####        print(n,"is prime number")
####else:
####    print(n,"is not prime number")
##
##
##
#### ************************************************************************************************************************************************************         
##n=int(input("enter a number"))
##a=1
##for i in range(1,n+1):
##    a=a*i
##print(a)

##*************************************************************************************************************************************************************

##n=int(input("enter a number"))
##for i in range(1,11):
##    a=n*i
##    print(i,'*',n,'=',a)

##******************************************************************************************************************************************************************

##to check given number is armstrong or not
##n=int(input("enter a number"))
##r=0
##q=n
##while n!=0:
##    b=n%10
##    r=r+b*b*b
##    n=n//10
##if q==r:
##    print(q,"is a armstrong")
##else:
##    print(q,"is not a armstrong")


##*******************************************************************************************************************************************************************

##find sum of n natural numbers
##n=int(input("enter the total number"))
##a=0
##for i in range(n+1):
##    a=a+i
##print(a)

##**************************************************************************************************************************************************************
####to display fibonacci series
##
##ft_num=0
##sec_num=1
##count=0
##n=int(input("enter the total number"))
##if n<1:
##    print("faco series is not possible")
##elif n==1:
##    print("fibonacii series is",ft_num)
##else:
##    print("fibonacii series are:")
##    while count<n:
##        print(ft_num)
##        c=ft_num+sec_num
##        ft_num=sec_num
##        sec_num=c
##        count=count+1


##****************************************************************************************************************************************************************
##display armstrong number between two given numbers

##l_num=int(input("enter the lower number"))
##u_num=int(input("enter the upper number"))
##for i in range(l_num,u_num+1):
##    d=0
##    temp=i
##    while temp>0:
##        r=temp%10
##        d+=r*r*r
##        temp//=10
##    if i==d:
##        print(d)
        
##*****************************************************************************************************************************************************************

## w.a.p.s. that will perform any one arithmatic operation for the given inputs based on the user choise if the choise is 1->add  if 2->sub if 3->mul if 4->div
####if 5->modul other wise display invalid choise


##print("user choise will be between 1 to 5 otherwise it will return invalide opration")
##a,b,choise=map(eval,input("enter a,b,choise value").split())
##if choise==1:
##    print(f"sum of {a},{b} is {a+b}")
##elif choise==2:
##    print(f"sub of {a},{b} is {a-b}")
##elif choise==3:
##    print(f"mul of {a},{b} is {a*b}")    
##elif choise==4:
##    print(f"div of {a},{b} is {a/b}")
##elif choise==5:
##    print(f"remainder of {a},{b} is {a%b}")
##else:
##    print("invalid operation")
##********************************************************************************************************************************************************
##w.a.p.s to sort given numbers in the ascending order

##a,b,c=map(int,input("enter a,b,c value").split())
##if a>b and a>c:
##    if b>c:
##        print(c,b,a)
##    else:
##        print(b,c,a)
##elif b>c:
##    if c>a:
##        print(a,c,b)
##    else:
##        print(c,a,b)
##else:
##    if a>b:
##        print(b,a,c)
##    else:
##        print(a,b,c)
##        
    
##*************************************************************************************************************************************************************

##to calculate the electricity bill based on following slabrates by reading oldmeter and newmeter
##0-100=2.5 rupee
##101-150=3.2 rupee
##151-200=5.8 rupee
##201-250=6.9
##251-300=7.3
##>300=9

##old_meter=eval(input("enter the old meter value"))
##new_meter=eval(input("enter the new meter value"))
##new_consumption=new_meter-old_meter
##if new_consumption<=100:
##    atm=new_consumption*2.5
##elif new_consumption<=150:
##    atm=new_consumption*3.2
##elif new_consumption<=200:
##    atm=new_consumption*5.8
##elif new_consumption<=250:
##    atm=new_consumption*6.9
##elif new_consumption<=300:
##    atm=new_consumption*7.3
##else:
##    atm=new_consumption*9
##print("total amount",atm)    


##**********************************************************************************************************************************************************

##bubble sort
##def bubble_sort(li):
##    for i in range(len(li)):
##        for j in range(i+1,len(li)):
##            if li[i]<li[j]:
##                li[i],li[j]=li[j],li[i]
##            else:
##                li[i],li[j]=li[i],li[j]
##                
##                
##li=[77,3,12,1]
##bubble_sort(li)
##for i in range(len(li)):
##    print(li[i])

##******************************************************************************************************************************************************

## to check three numbers are equal or not using nested if else

##a,b,c=map(int,input("enter a,b,c values").split())
##if a==b and a==c:
##    if b==c:
##        print("a,b,c values are equal")
##    else:
##        print("a,b,c values are not equal")
##else:
##    print("a,b,c values are not equal")
##**********************************************************************************************************************************************************

## print "hello" if a number entered user is a multiple of five other wise print Bye

##n=int(input("enter a value"))
##if n%5==0:
##    print("Hello")
##else:
##    print("Bye")
##
##********************************************************************************************************************************************************    
    
## w.a.p.s. to check the last digit of given number is divigiable by 3 or not
##n= eval(input("enter a number"))
##p=n%10
##if p%3==0:
##    print("last digit of given number is div by 3")
##else:
##    print("last digit of given number is not div by 3")
    
##***********************************************************************************************************************************************************************        

## w.a.p.s.to accept the cost price of a bike and display the road tax to be paid according to the folling criteria

##cost price               tax
##>100000                   15%
##>50000 and <= 100000      10%
##<=50000                   5%

##tax=0
##cost_price=eval(input("enter the cost of bike"))
##if cost_price<=50000:
##    tax=(5/100)*cost_price
##elif cost_price>=50000 and cost_price<= 100000:
##    tax=(10/100)*cost_price
##else:
##    tax=(15/100)*cost_price
##print("tax of your bike is :",tax)
##********************************************************************************************************************************************************
    
## w.a.p.s to check wether a number entered is three digit number  or not
##n=int(input("enter a number"))
##count=0
##while n!=0:
##    r=n%10
##    count=count+1
##    n=n//10
##if count==3:
##    print("entered number have three digit")
##else:
##    print(count)
    
##*************************************************************************************************************************************************************    

## accept the following from the user and calculate the percentage of class attended
##a. total number of working days
##b.total numberof days for absent
##after calculating persentage show that , if the percentage is less than 75, than student will not be able to sit in the exam


##wd=int(input("enter the total number of working days"))
##ad=int(input("enter the total number of absent days"))
##per=((wd-ad)/wd)*100
##print("percentage=",per)
##if per>=75:
##    print("this student is eligible for exam")
##else:
##    print("this student is not eligible for exam")
##***************************************************************************************************************************************************************************

## A company decided to give bonus to employee according to following criteria:
## time period of sevice         Bonus
## more than 10 years            10%
## >=6 aand <=10                  8%
## less than 6 years              5%
## ask to user for their salary and years of servies and print the net bonus amount


    
##salary=eval(input("enter the salary"))
##yr=eval(input("enter the years"))
##if yr<6:
##    bonus=(5/100)*salary
##elif yr>=6 and yr<=10:
##    bonus=(8/100)*salary
##elif yr>10:
##    bonus=(10/100)*salary
##print("net bonus for emplyees",bonus)    
    
##***********************************************************************************************************************************************************************************    
    
##w.a.p.s. to accept two numbers and mathematical operators and perform operation accordingly
##
##f_num=eval(input("enter the first value"))
##s_num=eval(input("enter the second value"))
##ope=input("enter the operation")
##if ope=="+":
##    print("sum of two numbers is:",(f_num+s_num))
##elif ope=="-":
##    print("sub of two numbers is:",(f_num-s_num))
##elif ope=="*":
##    print("mul of two numbers is:",(f_num*s_num))
##elif ope=="/":
##    print("float div  of two numbers is:",(f_num/s_num))    
##elif ope=="//":
##    print("int div of two numbers is:",(f_num//s_num))
##elif ope=="%":
##    print("modular div  of two numbers is:",(f_num%s_num))
##elif ope=="**":
##    print("power of two numbers is:",(f_num**s_num))
##else:
##    print("invalid operation")

##*****************************************************************************************************************************************************************

## accept three numbers from the user and display the second largest number

##a,b,c=map(int,input("enter a,b,c value").split())
##
##if a>b and a>c:
##    if b>c:
##        print(b,"second  grester")
##    else:
##        print(c,"second greater")
##elif b>c:
##    if a>c:
##        print(a,"second greater")
##    else:
##        print(c,"second greater")
##else:
##    if a>b:
##        print(a,"second greater")
##    else:
##        print(b,"second  grester")
##******************************************************************************************************************************************************************
        
## accept three sides of triangle and check whether the triangle is possible or not
##(triangle is possible only when sum of any two sides is greater than 3rd side)
##s1,s2,s3=map(int,input("enter the s1,s2,s3 sides of a triangle").split())
##if s1+s2>s3 and s2+s3>s1 and s1+s3>s2:
##    print("triangle is possible")
##else:
##    print("triangle is not possible")
    
##***********************************************************************************************************************************************************

##accept the number of days from the user and calculate the charge for library according to following
##till five days: Rs 2/day
##six to ten days: Rs 3/day
##11 to 15 days : Rs 4/day
##after 15 days : Rs 5/day

##days=int(input("enter the numbers of days"))
##if days<=5:
##    amt=2*days
##elif days>=6 and days<=10:
##    amt=3*days
##elif days>=11 and days<=15:
##    amt=4*days
##else:
##    amt=5*days
##print("total amount:",amt)    

##***************************************************************************************************************************************************************

##accept the kilometer covered and calculate the bill according to the following criteria:
##first 10km       RS 11/km
##next 90km        Rs 10/km
##after that       RS  9/km

##km=eval(input("enter the distance in km"))
##if km<=10:
##    amt=11*km
##elif km<=90:
##    amt=10*km
##else:
##    amt=9*km
##print("total amount:",amt)    

##*********************************************************************************************************************************************
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

####Use a loop to display elements from a given list present at odd index positions
##
##li=[10,20,30,40,50,60,70,80,90,100]
####p=len(li)
####
####for i in range(1,p,2):
####    print(li[i])
##
##for i in li[1::2]:
##    print(i)
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
##
##li=[10,20,30,40,50,60,70,80,90,100]
##p=len(li)
##
##for i in range(1,p,2):
##    print(li[i])

##for i in li[1::2]:
##    print(i)


##******************************************************************************************************************************************************************
##def selection_sort(li):
##    for i in range(len(li)):
##        min=i
##        for j in range(i+1,len(li)):
##            if li[j]<li[min]:
##                min=j
##                j=j-1
##        if min!=i:
##            li[min],li[i]=li[i],li[min]
##      
##li=[7,5,3,9]
##selection_sort(li)
##for i in range(len(li)):
##    print(li[i])

##**************************************************************************************************************************************************************
##
##for i in range(1,11):
##    print(i,end=" ")
##    if i==5:
##        print()
##***************************************************************************************************************************************************
##Python Program to Solve Quadratic Equation
##a,b,c=map(int,input("enter a,b,c,value").split())
##d=(b*b)-(4*a*c)
##p=d**0.5
##pr=(-b+p)/(2*a)
##nr=(-b-p)/(2*a)
##print("positive result",pr)
##print("negative result",nr)
##***********************************************************************************************************************

##Python Program to check given number is prime or not
##n=int(input("enter a value"))
##for i in range(2,n//2):
##    if n%i==0:
##        print("not prime")
##        break
##else:
##    print("prime")
##*****************************************************
##n=int(input("enter a value"))
##i=2
##while i<n:
##    if n%i==0:
##        print("not prime")
##        break
##    i=i+1
##else:
##    print("prime")
##*******************************************************
#Python Program to check given number is prime or not using flag
##n=int(input("enter a value"))
##flag=0
##for i in range(2,n//2+1):
##    if n%i==0:
##        print("not prime")
##        flag=1
##        break
##if flag==0:
##    print("prime")
##*************************************************************************************************************************
## python programs to print factors
##n=int(input("enter a value"))
##for i in range(1,n+1):
##    if n%i==0:
##        print(i)
##****************************************************        
##n=int(input("enter a value"))
##i=1
##while i<n+1:
##    if n%i==0:
##        print(i)
##    i=i+1
##************************************************************************************************************************
##python program to calculate sum of the factor of a given number
##n=int(input("enter a value"))
##s=0
##for i in range(2,n//2+1):
##    if n%i==0:
##        print(i)
##        s=s+i
##print("sum of the factors is",s)        
##******************************************************************************************************************
## to display sum of indivisual digits of a given number

##n=int(input("enter a number"))
##s=0
##while n>0:
##    r=n%10
##    s=s+r
##    n=n//10
##print("sum=",s)    

##******************************************************************************************************************************

##reverse a number
##n=int(input("enter a value"))
##while n>0:
##    r=n%10
##    print(r,end="")
##    n=n//10
    
##******************************************************
##n=int(input("enter a value"))
##rev=0
##while n>0:
##    r=n%10
##    rev=(rev*10)+r
##    n=n//10
##print(rev)
##****************************************************************************************************************
##python program to calculate GCD of two numbers
##a,b=map(int,input("enter a,b values").split())
##while b!=0:
##    r=a%b
##    if r==0:
##        print(b)
##        break
##    a=b
##    b=r
##***************************************************
##a,b=map(int,input("enter a,b values").split())
##while b!=0:
##    r=a%b
##    a=b
##    b=r
##print(a)    
##*****************************************************
##a,b=map(int,input("enter a,b values").split())
##
##if a>b:
##    m=b
##else:
##    m=a
##
##for i in range(m,1,-1):
##    if a%i==0 and b%i==0:
##        print(i)
##        break
##**********************************************************************************************************************
##python program to calculate LCM of two numbers
##a,b=map(int,input("enter a,b value").split())
##m=a
##n=b
##while b!=0:
##    r=a%b
##    if r==0:
##        c=b
##        break
##    a=b
##    b=r
##lcm=(m*n)//b
##print(lcm)
##***********************************************************************************************************    
##python program to count number of factor for a given number excluding 1 and n    

##n=int(input("enter a value"))
##count=0
##for i in range(2,n//2+1):
##    if n%i==0:
##        print(i)
##        count=count+1
##print("number of the factor",count)       
##*************************************************************************************       

##python program to check whether given number is prime or not based on factor
##n=int(input("enter a value"))
##count=0
##for i in range(2,n//2+1):
##    if n%i==0:
##        count=count+1
##if count==0:
##    print("prime")
##else:
##    print("not prime")
######***********************************************************************************************************
##a,b=map(int,input("enter a,b values").split())
##while b!=0:
##    r=a%b
##    if r==0:
##        c=b
##        break
##    a=b
##    b=r
##if c==1:
##    print("a and b are the co-prime of each other")
##else:
##    print("a and b are not co-prime of each other")
##    
##*****************************************************************************************************************************
##Inverted Pyramid of Numbers
##11111
##2222
##333
##44
##5
##n=int(input("enter a number"))
##for i in range(1,n+1):
##    for j in range(1,n+1):
##        if i<=j:
##            print(i,end=" ")
##    print()    
##********************************************************************************************************************        
##Inverted Pyramid of Descending Numbers
##5 5 5 5 5 
##
##4 4 4 4 
##
##3 3 3 
##
##2 2 
##
##1
##n=int(input("enter a number"))
##for i in range(n,0,-1):
##    for j in range(1,n+1):
##        if i>=j:
##            print(i,end=" ")
##    print()
##***********************************************************************************************************************
##Inverted Pyramid of the Same Digit
##5 5 5 5 5 
##
##5 5 5 5 
##
##5 5 5 
##
##5 5 
##
##5
##n=int(input("enter a number"))
##for i in range(n,0,-1):
##    for j in range(1,n+1):
##        if i>=j:
##            print("5",end=" ")
##    print()

##*****************************************************************************************************************
##Reverse Pyramid of Numbers
##Pattern:
##
##1 
##
##2 1 
##
##3 2 1 
##
##4 3 2 1 
##
##5 4 3 2 1
##n=int(input("enter a number"))
##for i in range(1,n+1):
##    for j in range(i,0,-1):
##        print(j,end=" ")
##          
##    print()    
##**************************************************************************************************************************
##Pyramid of Natural Numbers Less Than 10
##Pattern:
##
##1 
##
##2 3 4 
##
##5 6 7 8 9
##n=int(input("enter a number"))
##c=1
##for i in range(1,n+1,2):
##    for j in range(1,i+1):
##        if c<10:       
##            print(c,end=" ")
##            c=c+1  
##    print()  
####************************************************************************************************************************
##Reverse Pattern of Digits from 10 
##Pattern:
##1
##3 2
##6 5 4
##10 9 8 7
##n=int(input("enter a number"))
##c=1
##for i in range(1,n+1):
##    for j in range(1,i+1):
##        if c<=10:       
##            print(c,end=" ")    
##            c=c+1
##            
##    print()
##*************************************************
##start = 1
##stop = 2
##currentNumber = stop
##for row in range(2, 6):
##    for col in range(start, stop):
##        currentNumber -= 1
##        print(currentNumber, end=" ")
##    print()
##
##    start = stop
##
##    stop += row
##
##    currentNumber = stop
##**********************************************************************************************************
##Unique Pyramid Pattern of Digits
##Pattern:
##1 
##
##1 2 1 
##
##1 2 3 2 1 
##
##1 2 3 4 3 2 1 
##
##1 2 3 4 5 4 3 2 1
##n=int(input("enter a number"))
##for i in range(1,n+1):
##    for j in range(1,i+1):
##        print(j,end=" ")
##    for j in range(i-1,0,-1):
##        print(j,end=" ")    
##    print()    
##***************************************************************************************************************
##Connected Inverted Pyramid Pattern of Numbers
##Pattern:
##5 4 3 2 1 1 2 3 4 5 
##
##5 4 3 2 2 3 4 5 
##
##5 4 3 3 4 5 
##
##5 4 4 5 
##
##5 5
##n=int(input("enter a number"))
##for i in range(1,n+1):
##    for j in range(n,0,-1):
##        if i<=j:
##            print(j,end=" ")
##    for j in range(1,n+1):
##        if i<=j:
##            print(j,end=" ")        
##    print()    
##**********************************************************************************************************************
##Even Number Pyramid Pattern
##Pattern:
##10 
##10 8 
##10 8 6 
##10 8 6 4 
##10 8 6 4 2
##n=int(input("enter a number"))
##for i in range(10,0,-2):
##    for j in range(10,i-1,-2):
##        print(j,end=" ")
##    print()    
##****************************************************************************************************************************
##Pyramid of Horizontal Tables
##Pattern:
##0  
##0 1  
##0 2 4  
##0 3 6 9  
##0 4 8 12 16  
##0 5 10 15 20 25  
##0 6 12 18 24 30 36
##n=int(input("enter a number"))
##p=0
##for i in range(n+1):
##    for j in range(i+1):
##        print(j*p,end=" ")
##    p=p+1
##    print()
##**************************************************************************************************************************
##Pyramid Pattern of Alternate Numbers
##Pattern:
##1 
##3 3 
##5 5 5 
##7 7 7 7 
####9 9 9 9 9
##n=int(input("enter a number"))
##for i in range(1,n+1,2):
##    for j in range(1,i+1,2):
##        print(i,end=" ")
##    print()
##*********************************************************************************************************************
##Mirrored Pyramid (Right-angled Triangle) Pattern of Numbers
##Pattern:
##
##           1 
##
##         1 2 
##
##      1 2 3 
##
##   1 2 3 4 
##
## 1 2 3 4 5
##n=int(input("enter a number"))
##for i in range(1,n+1):
##    print(" "*(n-i),end="")
##    for j in range(1,i+1):
##        print(j,end="")
##    print()
##************************************************************************************************************************
##enter a number5
##1 2 3 4 5 
## 1 2 3 4 
##  1 2 3 
##   1 2 
##    1 
##n=int(input("enter a number"))
##for i in range(n,0,-1):
##    print(" "*(n-i),end="")
##    for j in range(1,i+1):
##            print(j,end=" ")
##    print()
##***********************************************************************************************************************
##enter a number5
##    1 
##   1 2 
##  1 2 3 
## 1 2 3 4 
##1 2 3 4 5
##n=int(input("enter a number"))
##for i in range(1,n+1):
##    print(" "*(n-i),end="")
##    for j in range(1,i+1):
##            print(j,end=" ")
##    print()
##**************************************************************************************************************
## Equilateral Triangle with Stars (Asterisk Symbol)
##Pattern:
##
##            *   
##           * *   
##          * * *   
##         * * * *   
##        * * * * *   
##       * * * * * *   
##      * * * * * * *

##n=int(input("enter a number"))
##for i in range(1,n+1):
##    print(" "*(n-i),end="")
##    for j in range(1,i+1):
##        print("*",end=" ")
##    print()    

##**********************************************************************************************************************
##Downward Triangle Pattern of Stars
##Pattern:
##        * * * * * * 
##         * * * * * 
##          * * * * 
##           * * * 
##            * * 
##             * 
##n=int(input("enter a number"))
##for i in range(n,0,-1):
##    print(" "*(n-i),end="")
##    for j in range(1,i+1):
##        print("*",end=" ")
##    print() 
##**************************************************************************************************************************
##Pyramid Pattern of Stars
##Pattern:
##* 
##* * 
##* * * 
##* * * * 
##* * * * *
##n=int(input("enter a number"))
##for i in range(n,0,-1):
##    print(" "*(n-i),end="")
##    for j in range(1,i+1):
##        print("*",end=" ")
####    print()
####************************************************************************************************************************************************
##n=int(input("enter a number"))
##for i in range(1,n+1):
##    print(" "*(n-i),end="")
##    for j in range(1,i+1):
##        if j==1:
##            print("1",end="")
##        else:
##            print(" ",end="")
##    for j in range(i-1,0,-1):
##        if j==1:
##            print(j,end="")
##        else:
##            print(" ",end="")
##    print()        
##for i in range(n-1,0,-1):
##    print(" "*(n-i),end="")
##    for j in range(1,i+1):
##        if j==1:
##            print(j,end="")
##        else:
##            print(" ",end="")
##    for j in range(i-1,0,-1):
##        if j==1:
##            print("1",end="")
##        else:
##            print(" ",end="")            
##    print()    
####**********************************************************************************************************************************************************
####w.a.p.s to print the only prime factors
##n=int(input("enter a number"))
##for j in range(2,n//2+1):
##    if n%j==0:
##        for i in range(2,j//2+1):
##            if j%i==0:
##                break
##        else:
##            print(j)
##********************************************************************************************************************************************************************                
##series:
##    3,5,9,11,15,17,21,..........
    
##n=int(input("enter a number"))
##c=3
##for i in range(1,n+1):
##    print(c,c+2,end="  ")
##    c=c+6
##**********************************************************************************************************************************************************
##n=int(input("enter the term"))
##a=3
##b=5
##c=9
##for i in range(3,n):
##    d=b+c-a
##    a=b
##    b=c
##    c=d
##print(d)        
##*********************************************************************************************************************************************************************    

##row=int(input("enter a number"))
##max_val=(row*(row+1))//2
##val=max_val- row+1
##i=0
##while(i<row):
##    j=0
##    col=row-i
##    while(j<col):
##        print(val+j,end=" ")
##        j=j+1
##    print()
##    val=val-(row-i-1)
##    i=i+1


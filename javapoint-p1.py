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
def bubble_sort(li):
    for i in range(len(li)):
        for j in range(i+1,len(li)):
            if li[i]>li[j]:
                li[i],li[j]=li[j],li[i]
            else:
                li[i],li[j]=li[i],li[j]
                
                
li=[77,3,12,1]
bubble_sort(li)
for i in range(len(li)):
    print(li[i])








































    
    
    
































































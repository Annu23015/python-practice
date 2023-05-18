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
##s="my name is raj kumar"
##p=s.split()
##for i in range(len(p)):
##    if i%2!=0:
##        x=p[i][::-1]
##        p[i]=x        
##print(p)        
##            

##**********************************************************************************************

##a="rhfusfjefhsf"
##repetation character will add at the last indexes
##output="rujehhssffff"
##******************************************************************************************************************    
        
##t=(1,2,3,4,5)
##print(t*2)
##print(t+t)
##***********************
##t1=(1,4,"cs","ip",5)
##print(t1)
##t=tuple(map(int,input("enter tuple element").split()))
##print(t)
##t1=(12,3,45,"hockey","anil",("a","b"))
##print(t1[0])
##print(t1[-1])
##print(t1[-1::-1])
##print(t1[4])
##print(t1[5][1])
##*********************************************************************************************
##t1=(1,2,3,4,5,6)                           { it will give error}
##print(sum(max(t1)+min(t1)))
##****************************************************************************************
##t1=()
##n=int(input("enter length of tuple"))
##for i in range(n):
##    n1=int(input("enter the numbers"))
##    t1=t1+(n1,)
##print(t1)    
##
##t1=(23,32,4,5,2,12,23,7,9)
##for i in range(3):
##    n=int(input("enter elements"))
##    t1=t1+(n,)
##print(t1)    

##write a program to swap given tuples
##t1=("a","b")
##t2=(34,65)
##t1,t2=t2,t1
##print(t1)
##print(t2)    
##*************************************************************************************************************************************************************

##Python program to create a list of tuples from given list having number and its cube in each tuple
##Input: list = [1, 2, 3]
##Output: [(1, 1), (2, 8), (3, 27)]
##l=list(map(int,input("enter list elements").split()))
##print(l)
##t=[]
##for i in l:
##    p=i**3
##    t.append((i,p))
##print(t)
##*********************************************************************************************************************************
##Modulo of tuple elements
##The original tuple 1 : (10, 4, 5, 6)
##The original tuple 2 : (5, 6, 7, 5)
##The modulus tuple : (0, 4, 5, 1)

##t1=tuple(map(int,input("enter tuple elements").split()))
##t2=tuple(map(int,input("enter tuple elements").split()))
##t3=()
##for i,j in zip(t1,t2):
##    m=i%j
##    t3=t3+(m,)
##print(t3)        
        
##for i in range(min(len(t1),len(t2))):
##    m=t1[i]%t2[i]
##    t3=t3+(m,)
##print(t3)    
##******************************************************************************************************************************    
##Row-wise element Addition in Tuple Matrix
##Input :
##test_list = [[(‘Gfg’, 3)], [(‘best’, 1)]]
##cus_eles = [1, 2]
##Output : [[(‘Gfg’, 3, 1)], [(‘best’, 1, 2)]]
##
##Input :
##test_list = [[(‘Gfg’, 6), (‘Gfg’, 3)]]
##cus_eles = [7]
##Output : [[(‘Gfg’, 6, 7), (‘Gfg’, 3, 7)]]

##l=[]
##n=int(input("enter no. of rows"))
##m=int(input("enter no. of rows"))
##for i in range(n):
##    s=[]
##    for j in range(m):
##        e=input("enter element")
##        print(e.isdigit())
##        if e.isdigit()==True:
##            s.insert(0,int(e))
##        else:
##            s.append(e)
##            
##            
##    l.append(s)
##print(l)    
    

##**************************************************************************************************************************************
##Update each element in tuple list
##The original list : [(1, 3, 4), (2, 4, 6), (3, 8, 1)]
##List after bulk update : [(5, 7, 8), (6, 8, 10), (7, 12, 5)]

##l=[]
##n=int(input("enter a number"))
##for i in range(n):
##    m=tuple(map(int,input("enter element").split()))
##    l.append(m)
##print(l)
##k=int(input("enter a element"))
##l1=[]
##for j in l:
##    t=tuple()
##    for a in j:
##        s=a+k
##        t=t+(s,)
##    l1.append(t)    
##        
##print(l1)       
##**********************************************************************************************************************************************************
## Multiply Adjacent elements
##The original tuple : (1, 5, 7, 8, 10)
##Resultant tuple after multiplication : (5, 35, 56, 80)
##t=tuple(map(int,input("enter a number").split()))
##t1=tuple()
##for i in range(len(t)-1):
##        s=t[i]*t[i+1]
##        t1=t1+(s,)
##print(t1)        
##******************************************************************************************************************************************        
##Join Tuples if similar initial element
##Input  : test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)] 
##Output : [(5, 6, 7, 8), (6, 10), (7, 13)] 
##Input  : test_list = [(5, 6), (6, 7), (6, 8), (6, 10), (7, 13)] 
##Output : [(5, 6), (6, 7, 8, 10), (7, 13)]
##l=[]
##t=tuple()
##n=int(input("enter a number"))
##for i in range(n):
##    l.append(tuple(map(int,input("enter element").split())))
##print(l)
##l1=[]
##for i in range(len(l)-1):
##    for j in range(len(l[i])):
##        if l[i][j]==l[i+1][j]:
##            s=l[i][j]
##            t=t+(s,)
##        t=t+(l[i][j+1],)    
##            
##l1.append(t)
##            
##            
##            
##print(l1)            
            
            

##**********************************************************************************************************************************************
##All pair combinations of 2 tuples
##Input : test_tuple1 = (7, 2), test_tuple2 = (7, 8) 
##Output : [(7, 7), (7, 8), (2, 7), (2, 8), (7, 7), (7, 2), (8, 7), (8, 2)] 
##Input : test_tuple1 = (9, 2), test_tuple2 = (7, 8) 
##Output : [(9, 7), (9, 8), (2, 7), (2, 8), (7, 9), (7, 2), (8, 9), (8, 2)]
##t1=tuple(map(int,input("enter elements").split()))
##t2=tuple(map(int,input("enter elements").split()))
##l=[]
##l1=[]
##t=tuple()
##for i in t1:
##    for j in t2:
##        t=(i,)+(j,)
##        l.append(t)
##for i in t2:
##    for j in t1:
##        t=(i,)+(j,)
##        l1.append(t)        
##print(l+l1)

##******************************************************************************************************************************
##Remove Tuples of Length K
##nput : test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)], K = 2 
##Output : [(4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)] 
##Explanation : (4, 5) of len = 2 is removed. 
##Input : test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)], K = 3 
##Output : [(4, 5), (4, ), (1, ), (3, 4, 6, 7)] 
##Explanation : 3 length tuple is removed.
##l=[]
##n=int(input("enter a number"))
##for i in range(n):
##    l.append(tuple(map(int,input("enter tuple element").split())))
##print(l)
##k=int(input("enter element"))
##for i in l:
##        if len(i)==k:
##            l.remove(i)
##print(l)
##*******************************************************************************************************************
## Remove Tuples from the List having every element as None
##Input : test_list = [(None, 2), (None, None), (3, 4), (12, 3), (None, )] 
##Output : [(None, 2), (3, 4), (12, 3)] 
##Explanation : All None tuples are removed.
##Input : test_list = [(None, None), (None, None), (3, 4), (12, 3), (None, )] 
##Output : [(3, 4), (12, 3)] 
##Explanation : All None tuples are removed. 

##l=[]
##l1=[]
##n=int(input("enter a number"))
##for i in range(n):
##    l.append(tuple(map(str,input("enter tuple elements").split())))
##print(l)    
##for i in range(len(l)):
##    if l[i]=='None':
##        l1.append(l[i])    
##print(l1)        
##s=input("entera string")
##k=input("enter substring")
##print(s.index('a',2,len(s)-1))
##for i in range(len(s)-len(k)+1):
##    for j in range(len(k)):
##        if s[i+j]!=k[j]:
##            break
##    else:
##        print(i)
##        
##else:
##    print(-1)
##*************************************************************************************************      
##given string palindrom or not
##s=input("enter a string").lower()
##if s==s[::-1]:
##    print("palindrom")
##else:
##    print("not")
##************************************************
##s=input("enter a string").lower()
##i=0
##j=len(s)-1
##while i<j:
##    if s[i]!=s[j]:
##        print("not palindrom")
##        break
##    i=i+1
##    j=j-1
##else:
##    print("palindrom")
##**********************************************************************************************************************
##w.a.p.s to reverse a string without reversing the special symbol
##s=list(input("enter a sting"))
##i=0
##j=len(s)-1
##while i<j:
##    if not s[i].isalnum():
##        i=i+1
##    elif not s[j].isalnum():
##        j=j-1
##    else:
##        s[i],s[j]=s[j],s[i]
##        i=i+1
##        j=j-1
##print("".join(s))        

##*******************************************************************************************************************

##s=input("enter a string")
##l=[]
##for i in s:
##    if i.isdigit():
##        l.append(i)
##l.sort(reverse=True)
##for j in range(len(l)-1,-1,-1):
##    if int(l[j])%2==0:
##        l.append(l.pop(j))
##        print("".join(l))
##        break
##else:
##    print(-1)

##*****************************************************************************************************************
##w.a.p.s. to return super reduced string

##s=list(input())
##i=0
##while i<(len(s)-1):
##    if s[i]==s[i+1]:
##        del s[i]
##        del s[i]
##        i=0
##    else:
##        i=i+1
##if len(s)==0:
##    print("empty string")
##else:
##    print("".join(s))
        
##**************************************************************************************************************
##w.a.p.s to check  pangram or not
##s=input().lower()
##
##for i in range(ord('a'),ord('z')):
##    if chr(i) not in s:
##        print("not pangram")
##        break
##else:
##    print("pangram")
##*********************************************************************************************************************
##w.a.p.s to check anagram or not
##s1=input()
##s2=input()
##if len(s1)==len(s2):
##    for i in s1:
##        s2=s2.replace(i,"",1)
##    if len(s2)==0:
##        print("anagram")
##    else:
##        print("not anagram")
##else:
##    print("not anagram")
##*************************************************
##s1=list(input())
##s2=list(input())
##s1.sort()
##s2.sort()
##if s1==s2:
##    print("anagram")
##else:
##    print("not")

##***************************************************
##s1=input()
##s2=input()
##for i in set(s1):
##    if s1.count(i)!=s2.count(i):
##        print("no")
##        break
##else:
##    print("yes")

##**********************************************************************************************************************
##w.a.p.s.to count frequency of every word and display b5a3c3d2g1h1e1

##s=input()
##l1=[]
##l2=[]
##for i in set(s):
##    c=s.count(i)
##    l1.append(i)
##    l1.append(c)
##print(*l1)
##********************************************************************************************************    
##s=input().lower()
##d=dict(zip([chr(i) for i in range(ord('a'),ord('z')+1)],range(1,27)))
##w=0
##i=0
##j=len(s)-1
##while i<j:
##    w=w+abs(d[s[i]]-d[s[j]])
##    i=i+1
##    j=j-1
##if i==j:
##    w=w+d[s[i]]
##print(w)
##**************************************************************************************************************
##s=input().split().lower()
##d=dict(zip([chr(i) for i in range(ord('a'),ord('z')+1)],range(1,27)))
##l=[]
##for k in s:
##  w=0
##  i=0
##  j=len(k)-1
##  while i<j:
##    w=w+abs(d[k[i]]-d[k[j]])
##    i=i+1
##    j=j-1
##  if i==j:
##    w=w+d[k[i]]
##  l.append(str(w))
##print(''.join(l))
##**************************************************************************************************************************************    
##s=input()
##d=dict(zip([i for i in s],[s.count(j) for j in s]))
##d=sorted(d.items(),key=lambda x: x[1],reverse=True)
##s=str()
##for i in d:
##    for j in i:
##        s=s+str(j)
##print(s)        
##**************************************************************************************************
##s=input()
##d=dict(zip([i for i in s if i.isalpha()],[i for i in s if i.isdigit()]))
##print(d)
##for i,j in d.items():
##    if d[s[i]]!=0:
##        print(i)   
##    j=j-1
    
##***************************************************************************************************        
## Write a python program to sort letters of word by lower to upper case format.
##Hint 
##Input:
##Enter a String:  pytHOnloBBy
##
##Expected output
##Result: p y t n l o y H O B B        
##        
##s=input()
##l=[]
##l1=[]
##for i in s:
##    if i.islower():
##        l.append(str(i))
##    else:
##        l1.append(str(i))
##print("".join(l+l1))
##****************************************************************************************************************************
##Write a program in Python to count lower, upper, numeric and special characters in a string.
##Given x = @pyThOnlobb!Y34
##
##Expected output
##Numeric counts 2
##Lower counts 8
##Upper counts 3
##Special counts 2
##s=input()
##c=0
##c1=0
##c2=0
##c3=0
##for i in s:
##    if i.isupper():
##        c=c+1
##    elif i.islower():
##        c1=c1+1
##    elif i.isdigit():
##        c2=c2+1
##    else:
##        c3=c3+1
##print("upper=",c)        
##print("lower=",c1)
##print("digit=",c2)
##print("special symbol=",c3)


##patterns
##11 12 13 14 15
##7   8  9 10
##4   5  6
##2   3
##1
##c=1
##l=[]
##n=int(input("enter a number"))
##for i in range(n):
##    a=''
##    num=0
##    while num<i+1:
##        a=a+str(c)+" "
##        c=c+1
##        num=num+1
##    l.append(a)
##for i in range(len(l)-1,-1,-1):
##    print(l[i])
##***************************************************************************************************************
##patterns:
##    01 06 11 16 21
##    02 07 12 17 22
##    03 08 13 18 23
##    04 09 14 19 24
##    05 10 15 20 25
##n=int(input("enter a number"))
##for i in range(1,n+1):
##    c=i
##    for j in range(1,n+1):
##        print("{:02d}".format(c),end=" ")
##        c=c+n
##    print()    
##****************************************************************************************************************************
##patterns:
##    15 14 13 12 11
##    10 09 08 07
##    04 05 06
##    03 02
##    01
##n=int(input("enter a number"))
##c=15
##for i in range(1,n+1):
##    for j in range(n,0,-1):
##        if i<=j:
##            print("{:02d}".format(c),end=" ")
##            c=c-1
##    print()
##*******************************************************************************************************
##print:
##    3 5 9 11 17 21 23 27..................
##*****************************************************************************************************
##w.a.p.s. to print nth term prime number
##n=int(input("enter the large number of the sequence"))
##t=int(input("enter the term"))
##count=0
##for i in range(2,(2*t+1)):
##    for j in range(2,i//2+1):
##        if i%j==0:
##            break
##    else:
##        count=count+1
##        if count==t:
##            print(i)

##***************************************************************************************

##count=int(input("enter the nth number"))
##if count==0:
##    print("count should not be zero")
##    quit()
##elif count=="1":
##    print("2")
##else:
##    count=count-1
##    num=3
##    while count!=0:
##        for i in range(2,num):
##            if num%i==0:
##                break
##        else:
##            count=count-1
##        num=num+1
##print(num-1)                
##************************************************************************************************************
##print:
##    3 5 9 11 15 17 21 23 27..................
##n=int(input("enter a number"))
##c=3
##while c<n:
##    print(c,c+2,end=" ")
##    c+=6

##*************************************************************************************************************
##find the maximum digit from a given number
##n=int(input("enter a number"))
##m=0
##while n!=0:
##    r=n%10
##    if r>m:
##        m=r
##    n=n//10    
##print(m)
##*******************************************************************************************************************
##find the minimum digit from a given number
##n=int(input("enter a number"))
##min=n%10
##while n!=0:
##    r=n%10
##    if r<min:
##        min=r
##    n=n//10    
##print(min)        
##**************************************************************************************************************************
##w.a.p.s.to print the only prime factor
##n=int(input("enter a number"))
##
##for i in range(2,n+1):
##    if n%i==0:
##        for j in range(2,i//2+1):
##            if i%j==0:
##                break
##        else:
##            print(i)
##**********************************************************************************************************************
##w.a.p.s to display nearest prime number p for the given number n where p>=n
##n=int(input("inter a number"))
##while True:
##    for i in range(2,n//2+1):
##        if n%i==0:
##            n=n+1
##            break
##    else:
##        print(n)
##        break
##************************************************************************************************************
##w.a.p.s to display nearest palindrom prime number p for the given number n where p>n 
##n=int(input("enter a number"))
##while True:
##    for i in range(2,n//2+1):
##        if n%i==0:
##            n=n+1
##            break
##    else:
##        t=n
##        rev=0
##        while t!=0:
##            r=t%10
##            rev=(rev*10)+r
##            t=t//10
##        if n==rev:
##            print(n)
##            break
##        else:
##            n=n+1
##**********************************************************************************************************************        
##w.a.p.s to diplay sum of individual digits of given number until you get a single number
##n=int(input("enter a number"))
##while n>9:
##    s=0
##    while n!=0:
##        r=n%10
##        s=s+r
##        n=n//10
##    n=s
##print(n)    
        
##********************************************************************************************************************    

####w.a.p.s to sort a number
##n=int(input("enter a number"))
##mn=0
##while True:
##    
##*********************************************************************************************************************
##l=[2,33,222,14,25]
##print(l[:-1])

##t=(1,2,4,3)
##print(t[3])
##************************************************************************************************************************
##even function
##def iseven(n):
##    if n%2==0:
##        return True
##    else:
##        return False
##n=int(input("enter a number"))    
##print(iseven(n))
##********************************************************************************************************************
##sum of even numbers
##def iseven(n):
##    if n%2==0:
##        return True
##    else:
##        return False
##def isodd(n):
##    if n%2!=0:
##        return True
##    else:
##        return False    
##p=int(input("enter a number"))
##s=0
##s1=0
##for i in range(2,p+1):
##    if iseven(i):
##        s=s+i
##    if isodd(i):
##        s1=s1+i
##print(s)        
##print(s1)
##***************************************************************************************************
##odd function
##def isodd(n):
##    if n%2!=0:
##        return True
##    else:
##        return False
##
##n=int(input("enter a number"))    
##print(isodd(n))    
##***********************************************************************************************************
##def factors(n):
##    f=0
##    for i in range(2,n//2+1):
##        if n%i==0:
##            l.append(i)
##            f=f+1
##            
##    else:
##        if f==0:
##            return 0
##    return (l)
##l=[]        
####print(factors(13))        
##n=int(input("enter a number"))
##print(sum(factors(n)))        

##s=sum(factors(n))
##if s==n:
##    print("perfect")
##elif s<n:
##    print("defficient")
##else:
##    print("abundent")
    
##******************************************************************************************************************


































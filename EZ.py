# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 23:26:40 2015

@author: Bella
"""

#1 Remove 

class solution:
    def removeElement(self,A,v):
        i=0
        while i <len(A):
            if A[i]==v:
                del A[i]
            else:
                i+=1
        return A

#2 Remove duplicate
    def removeDup(self, x):
        if len(x)==0:
            return 0
        a=[]
        for i in range(len(x)):
            if x[i] not in a:
                a.append(x[i])
            else:
                continue
        return a            

    def removeDup2(self,x):
        if len(x)==0:
            return 0
        front,back=1,1
        while front<len(x):
            if x[front]!=x[front-1]:
                x[back]=x[front]
                back+=1
            front+=1
        return back


#3 Unique number
    def getsingle(self, x):
        if len(x)==0:
            return 0
        a=[]
        for i in range(len(x)):
            if x[i] not in a:
                a.append(x[i])
            else:
                continue
        aa=a*2 
        return sum(aa)-sum(x)

#4 Move zeroes
    def movezero(self,x):
        a=[]
        b=[]
        i=0
        while i<len(x):
            if x[i]!=0:
                a.append(x[i])
            else:
                b.append(x[i])
            i+=1
        a.sort
        return a+b

    def movezero2(self,x):
        i,j=0,0
        while i<len(x):
            if x[i]==0:
                while (x[j]==0 & j+1<len(x)):  ###keep increase index
                        j+=1
                x[i],x[j]=x[j],x[i]       ##switch!!
            else:
                j+=1
            i+=1
        return x
            
#5 Zigzag

    def zigzag(self,x,n):
        r=range(2,n)
        r.reverse()
        i=(range(1,n+1)+r)*int(len(x)/n)+range(1, len(x)%n+1)
        t=[]
        b=lambda (aa,bb):bb;a=lambda (aa,bb):aa
        for p in range(1,n+1):
            tt=0
            while tt<len(x):
                if [b(q) for q in zip(x,i)][tt]==p:
                    t.append([a(q) for q in zip(x,i)][tt])
                tt+=1
        t="".join(t)
        return t
            
            
#6 Climb stair                         Dynamic Programming

    def climbstair(self,n):
        sol=[1 for i in range(n+1)]
        for i in range(2,n+1):
            sol[i]=sol[i-1]+sol[i-2]
        return sol[n]
        

#7 Ugly number

    def ugly(self,p):
        if p<=0:
            return False
        for n in [2,3,5]:
            while p%n==0:
                p/=n
        return p==1
 
#8 Excel       

    def exc(self,p):
        tmp=0
        for i in p:
            tmp=tmp*26+ord(i)-ord("A")+1
        return tmp
        
#9 Add digital

    def adddigit(self,d):
        num=0
        d=str(d)
        while len(d)!=1:
            for i in d:
                num+=int(i)
            d=str(num)
        return d


    def adddigit(self,d):
        num=0
        d=str(d)
        for i in d:
            num+=int(i)
        num2=0
        while num>9:
            for i in str(num):
                num2+=int(i)
            num=num2
        return num     
        
#10 Reverse integer

    def rint(self,t):
        if t>=0:
            tt=str(t)[::-1]
        else:
            tt=str(abs(t))[::-1]
            tt=['-']+[tt]
        return int(''.join(tt))

#11 Majority

    def maj(self,a):
        n=len(a)
        for i in a:
            if a.count(i)>n/2:
                break
        return i
                
#12 Happy number

    def happyn(self,n):
        n=str(n)
        num=0
        for i in n:
            num+=int(i)**2
        num2=0
        while num!=1:
            for i in str(num):
                num2+=int(i)**2
            num=num2
            
        #(while num>0:
        ##        num2+=(num % 10)**2
        #        num=num/10)            
               
        if num==1:
            return True
        else:
            return False
            
#13 House robber                        (Dynamic Programming)

    def houserob(self,num):
        option1,option2=0,0
        for i in num:
            option1,option2=max(option1,option2),option1+i
        return max(option1,option2)
    
    def houserob2(self,num):
        dp=[0]*(len(num)+1)
        for i in range(2,len(num)+1):
            dp[i]=max(dp[i-1],dp[i-2]+num[i-1])
        return dp[len(num)]
        
#14 Valid arg                          (HASH TABLE using dict)

    def anagram(self,wd1,wd2):
        l={}
        for i in wd1:
            if i not in l.keys():
                l[i]=1
            else:
                l[i]+=1
        ll={}
        for j in wd2:
            if i not in ll.keys():
                ll[j]=1
            else:
                ll[j]+1
        return l==ll
        
#15 Merge two list   LINKED LIST
        
#16 Length of lastword

    def lenoflwd(self,s):
        return len(s.split()[::-1][0])
        
#17 Palindrome number

    def palindrome(self,n):
        i=1
        while (n/(10**i))>10:          
            lft=n
            while lft>10**i:
                lft/=10
            lft%=10**(i-1)
                
            rt=n%10**i
            rt/=10**(i-1)
            
            if lft!=rt:
                return False
            i+=1
        return True
     #two index
    def check_palindrome(n) :
            strn = str(n)
            start=0; end=len(strn)-1
            while start <= end:
                    if strn[start] != strn[end]:
                            return 0
                    start+=1; end-=1
                   
            return 1 

#18 Palindrome linkedlist

#19 Duplicate

    def dup(self,n):
        if len(n)>len(set(n)):
            False
        else:
            True
            
#20 Nim Game                                 #observation

    def nim(self,n):
        return n//4!=0
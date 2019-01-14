import pickle
import os
import testproj3
from lucky import *
class scard:
    def __init__(self,name,phone,points,idno):
        self.name=name
        self.phone=phone
        self.points=points
        self.idno=idno

    def __str__(self):
        return str(self.idno)+","+self.name+","+self.phone+","+str(self.points)
smartcard={1001:["Bargavi","0569161887",1000],1002:["Anushree","0562770805",1000],1003:["Abolee","0563006076",452],1004:["Amarpreet","0563628501",255],1005:["Bharini","0502766028",362],1006:["Chandini","0566525465",352]}

class caty:
    
    def __init__(self,d1,d2,d3,d4,d5):
        

        self.d1=d1
        self.d2=d2
        self.d3=d3
        self.d4=d4
        self.d5=d5
    def print1(self):
        for i in self.d1:
            print i,self.d1[i]
        print
    def print2(self):
        for i in self.d2:
            print i,self.d2[i]
        print
    def print3(self):
        for i in self.d3:
            print i,self.d3[i]
        print
    def print4(self):
        for i in self.d4:
            print i,self.d4[i]
        print
    def print5(self):
        for i in self.d5:
            print i,self.d5[i]
        print

        
def calling():
       f1=open("cat.dat","rb")
       try:
          while True:
               s=pickle.load(f1)
               s.print1()
               s.print2()
               s.print3()
               s.print4()
               s.print5()
              
       except EOFError:
              pass
       f1.close()
def checking():
    f1=open("cat.dat","rb")
    f2=open("cat2.dat","wb")
    icode=input("Enter the item code")
    r=0
    if icode!=0:
        try:
            while True:
               s=pickle.load(f1)
               if s.d1.has_key(icode)==True:
                       r=s.d1
               elif s.d2.has_key(icode)==True:
                       r=s.d2
               elif s.d3.has_key(icode)==True:
                       r=s.d3
               elif s.d4.has_key(icode)==True:
                       r=s.d4
               elif s.d5.has_key(icode)==True:
                       r=s.d5
               if r!=0:
                   print "\n", r[icode], "\n"
                   o=input("Amount to be bought")
                   r[icode]["Availability"]+=o
                   print "\n", r[icode], "\n"
                   pickle.dump(s,f2)
               else:
                   pickle.dump(s,f2)
        except EOFError:
              pass
    f1.close()
    f2.close()
    os.remove("cat.dat")
    os.rename("cat2.dat","cat.dat")

def deleted():
    f1=open("cat.dat","rb")
    f2=open("cat2.dat","wb")
    icode=input("Enter the item code")
    r=0
    ch="n"
    if icode!=0:
        try:
            while True:
               s=pickle.load(f1)
               if s.d1.has_key(icode)==True:
                       s.d1=change(s.d1,icode)
                       ch="y"
               elif s.d2.has_key(icode)==True:
                       s.d2=change(s.d2,icode)
                       ch="y"
               elif s.d3.has_key(icode)==True:
                       s.d3=change(s.d3,icode)
                       ch="y"
               elif s.d4.has_key(icode)==True:
                       s.d4=change(s.d4,icode)
                       ch="y"
               elif s.d5.has_key(icode)==True:
                       s.d5=change(s.d5,icode)
                       ch="y"
               
               pickle.dump(s,f2)
        except EOFError:
              pass
    if ch=="n":
        print "Item not found"

    f1.close()
    f2.close()
    os.remove("cat.dat")
    os.rename("cat2.dat","cat.dat")

                    
def added():
    f1=open("cat.dat","rb")
    f2=open("cat2.dat","wb")
    
    item=raw_input("Enter item")
    cate=raw_input("Enter category")
    price=input("Price")
    ava=input("Availability")
    r=0
    c=num()
    try:
        while True:
           s=pickle.load(f1)
           
           a=c.next()
           b=c.next()
           if cate.lower()=="cosmetics":
                   s.d1[a]={"Product":item,"Price":price,"Availability":ava}
           elif cate.lower()=="electronics":
                   s.d2[a]={"Product":item,"Price":price,"Availability":ava}
           elif cate.lower()=="stationary":
                   s.d3[a]={"Product":item,"Price":price,"Availability":ava}
           elif cate.lower()=="clothes":
                   s.d4[a]={"Product":item,"Price":price,"Availability":ava}
           elif cate.lower()=="toileteries":
                   s.d5[a]={"Product":item,"Price":price,"Availability":ava}        
           pickle.dump(s,f2)
    except EOFError:
        pass
    f1.close()
    f2.close()
    os.remove("cat.dat")
    os.rename("cat2.dat","cat.dat")
        
def num():
    f3=open("sixty.txt","r")
    
    c=f3.read()
    f3.close()
    
    c=int(c)
    
    while True:
        yield c
        c+=1
        f3=open("sixty.txt","w")
        
        f3.write(str(c))
        f3.close()

        
def payment():
    calling()
    tp=0
    
    r=0
    while True:
           icode=input("Enter the item code")
           
           if icode!=0:
                 f1=open("cat.dat","rb")
                 f2=open("cat2.dat","wb")
                 
                 try:
                   while True:

                       
                       s=pickle.load(f1)
                       if s.d1.has_key(icode)==True:
                               r=s.d1
                       elif s.d2.has_key(icode)==True:
                               r=s.d2
                       elif s.d3.has_key(icode)==True:
                               r=s.d3
                       elif s.d4.has_key(icode)==True:
                               r=s.d4
                       elif s.d5.has_key(icode)==True:
                               r=s.d5
                       if r!=0:
                              q=input("Enter quantity")
                              if r[icode]["Availability"]>=q:
                                   p=r[icode]["Price"]
                                   r[icode]["Availability"]-=q
                                   tp+=p*q
                                   pickle.dump(s,f2)
                              else:
                                  print "Not Available"
                                  pickle.dump(s,f2)
                       else:
                          pickle.dump(s,f2)
                 except EOFError:
                     pass
                 f1.close()
                 f2.close()
                 os.remove("cat.dat")
                 os.rename("cat2.dat","cat.dat")
           else:
               break
    if tp!=0:    
            ch="nd"
            while ch!="d":
                  print "Total price=",tp
                  print "       MODE OF PAYMENT"
                  print "       1)pay by cash"
                  print "       2)pay by card"
                  print "       3)pay by RoyalCard points"
                  a=input("enter choice")
                  if a==1:
                     while True:
                         i=input("enter cash given")
                         if i>=tp:
                              c=i-tp
                              print "\n","Change:", c,"\n"
                              break
                         else:
                              print "Please pay the required amount"
                    
                     ch="d"
                  elif a==2:
                      i=input("Enter card number")
                      ch="d"
                  elif a==3:
                      i=input("Enter RoyalCard id number")
                      r=5*tp
                      ch=testproj3.checkout1(r,i)
            if a!=3:
                  print "\n","Are you a RoyalCard member?", "\n"
                  f=raw_input("Yes/No")
                  if f.lower() in "yes":
                       idno=input("Enter idno:")
                       testproj3.addp(idno,tp)
                       
            else:
                  testproj3.addp(i,tp)

            if tp>=500:
                print "You are eligible for LUCKY DRAW! Wanna try?"
                ans=raw_input("Yes/No")
                if ans.lower()=="yes":
                    times=tp/500
                    z=times
                    for i in range (times):
                        a=raw_input( "Press enter to test your luck! And any other character key to exit!")
                        print "No. of tries left=",z-1
                        
                        if a=="":
                            draw()
                            z-=1
                        else:
                            break
                        
            print "\n","!!!!!!!!THANK YOU!!!!!!!!!","\n"
            print "\n","!!!!!!!Come Again!!!!!!!!!", "\n"
            return smartcard
    
def view():
    
    while True:
        print "        1. Cosmetics"
        print "        2. Electronics"
        print "        3. Stationary"
        print "        4. Clothes"
        print "        5. Toileteries"
        print "        6. Exit"

        n=input("Enter your choice")
        if n==1:
            f1=open("cat.dat","rb")
            try:
               while True:
                   s=pickle.load(f1)
                   s.print1()
            except EOFError:
                pass
            f1.close()
        elif n==2:
            f1=open("cat.dat","rb")
            try:
               while True:
                   s=pickle.load(f1)
                   s.print2()
            except EOFError:
                pass
            f1.close()
        elif n==3:
            f1=open("cat.dat","rb")
            try:
               while True:
                   s=pickle.load(f1)
                   s.print3()
            except EOFError:
                pass
            f1.close()
        elif n==4:
            f1=open("cat.dat","rb")
            try:
               while True:
                   s=pickle.load(f1)
                   s.print4()
            except EOFError:
                pass
            f1.close()
        elif n==5:
            f1=open("cat.dat","rb")
            try:
               while True:
                   s=pickle.load(f1)
                   s.print5()
            except EOFError:
                pass
            f1.close()
        else:
            break
    

            
print "Welcome to STARSHOPPER HYPERMARKET!!"
while True:
    print " 1) Admin\n 2) Customer \n 3) Exit"
    a=input("Enter login option")
    if a==1:
        while True:
            print "        1) RoyalCard modifications"
            print "        2) Catalogue modifications"
            print "        3) Payment Counter"
            print "        4) Exit"
            b=input("Enter choice")
            if b==1:
                testproj3.smartcard2()
            elif b==2:
                while True:
                    print "1) Restock"
                    print "2) Add an item"
                    print "3) Delete an item"
                    print "4) Exit"
                    c=input("Enter choice")
                    if c==1:
                        checking()
                    elif c==2:
                        added()
                    elif c==3:
                        deleted()
                    elif c==4:
                        break
            elif b==3:
               payment()
            else:
                break
    elif a==2:
        while True:
            print "        1) View RoyalCard details"
            print "        2) View Catalogue"
            print "        3) Exit"
            b=input("Enter Choice")
            if b==1:
                testproj3.viewdet()
                    
            elif b==2:
                view()
            else:
                break
        
        
    else:
        break

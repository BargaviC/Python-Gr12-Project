import pickle
import os
class scard:
    def __init__(self,name,phone,points,idno):
        self.name=name
        self.phone=phone
        self.points=points
        self.idno=idno

    def __str__(self):
        return str(self.idno)+","+self.name+","+self.phone+","+str(self.points)
def create():
    f=open("scard.dat","wb")
    smartcard={1001:["Bargavi","0569161887",1000],1002:["Anushree","0562770805",1000],1003:["Abolee","0563006076",452],1004:["Amarpreet","0563628501",255],1005:["Bharini","0502766028",362],1006:["Chandini","0566525465",352]}
    for i in smartcard:
        idno=i
        name=smartcard[i][0]
        phone=smartcard[i][1]
        points=smartcard[i][2]
        print idno,name,phone,points

        S=scard(name,phone,points,idno)
        pickle.dump(S,f)
    f.close()

def adder():
    f=open("scard.dat","rb")
    d={}
    try:
        while True:
            s=pickle.load(f)
            d[s.idno]=[s.name,s.phone,s.points]
    except EOFError:
        pass

    f.close()
    f=open("scard.dat","ab")
    l=d.keys()
    l.sort()
    key=l[-1]+1
    
    name=raw_input("enter name")
    contactno=raw_input("enter mobile number/contact number")
    points=0
    
    info=list([name,contactno,points])
    s=scard(name,contactno,points,key)
    pickle.dump(s,f)
    
    print
    print "Your new information:"
    print "ID number:", key
    print "Name:", name
    print "Contact number:", contactno
    print "Current point:", points
    f.close()
def view():
    f=open("scard.dat","rb")
    d={}
    try:
        while True:
            s=pickle.load(f)
            d[s.idno]=[s.name,s.phone,s.points]
    except EOFError:
        pass
    print d
def viewdet():
    i=input("idno")
    f=open("scard.dat","rb")
    b="n"
    try:
        while True:
            s=pickle.load(f)
            if s.idno==i:
                print s
                b="y"
    except EOFError:
        if b=="n":
            print "not found"
        pass
def delete(idno):
    f=open("scard.dat","rb")
    f1=open("s1.dat","wb")
    
    try:
        while True:
            s=pickle.load(f)
            if s.idno!=idno:
                pickle.dump(s,f1)
    except EOFError:
        pass
    print "Deleted"
    f.close()
    f1.close()
    os.remove("scard.dat")
    os.rename("s1.dat","scard.dat")

def deletefunc():
    idno=input("input the idno to be deleted")
    f=open("scard.dat","rb")
    ch="d"
    try:
        while True:
            s=pickle.load(f)
            if s.idno==idno:
                n=s.name
                ch="nd"
    except EOFError:
        pass
    if ch=="d":
        print "Member not found"
        deletefunc()
    f.close()
    print "Are you sure you want to delete this person?:", n
    a=raw_input("Yes/No")
    if a.lower() in "yes":
        delete(idno)
    elif a.lower() in "no":
        pass
    
        
def addp(idno,tp):
    
    p=tp/20.0
    f=open("scard.dat","rb")
    f1=open("s1.dat","wb")
    try:
        while True:
            s=pickle.load(f)
            if idno==s.idno:
                points=s.points+p
                p=scard(s.name,s.phone,points,s.idno)
                pickle.dump(p,f1)
            else:
                pickle.dump(s,f1)
    except EOFError:
        pass
    
    f.close()
    f1.close()
    os.remove("scard.dat")
    os.rename("s1.dat","scard.dat")
def modifyname():
    idno=input("enter idno")
    nna=raw_input("enter new name")
    f=open("scard.dat","rb")
    f1=open("s1.dat","wb")
    ch='n'
    try:
        while True:
            s=pickle.load(f)
            if idno==s.idno:
                p=scard(nna,s.phone,s.points,s.idno)
                pickle.dump(p,f1)
                ch='y'
            else:
                pickle.dump(s,f1)
    except EOFError:
        pass
    if ch=='n':
        print idno," Not found"
    f.close()
    f1.close()
    os.remove("scard.dat")
    os.rename("s1.dat","scard.dat")

def modifyno():
    idno=input("enter idno")
    n=raw_input("enter new number")
    f=open("scard.dat","rb")
    f1=open("s1.dat","wb")
    ch='n'
    try:
        while True:
            s=pickle.load(f)
            if idno==s.idno:
                p=scard(s.name,n,s.points,s.idno)
                pickle.dump(p,f1)
                ch='d'
            else:
                pickle.dump(s,f1)
    except EOFError:
        pass
    if ch=='n':
        print idno, " Not found"
    f.close()
    f1.close()
    os.remove("scard.dat")
    os.rename("s1.dat","scard.dat")


def smartcard2():
    "'smart card values of format idno.:[name,contact,points]'"
    while True:
        print "        1)To add a new RoyalCard member"
        print "        2)To remove a RoyalCard member"
        print "        3)To change details of RoyalCard member"
        print "        4) Exit"
        a=input("Enter choice")
        if a==1:
            adder()
        elif a==2:
            deletefunc()
        elif a==3:
            print "        1) To Modify Name"
            print "        2) To modify Contact Number"
            c=input("enter choice")
            if c==1:
                modifyname()
            elif c==2:
                modifyno()
        else:
            break
def checkout1(r,i):
    nf=open("scard.dat","rb")
    nnf=open("s1.dat","wb")
    u="d"
    try:
        while True:
            s=pickle.load(nf)
            if s.idno==i:
                if s.points>=r:
                    p=s.points-r
                    r=scard(s.name,s.phone,p,s.idno)
                    pickle.dump(r,nnf)
                else:
                    print "Not enough points!!"
                    pickle.dump(s,nnf)
                    u="nd"
            else:
                pickle.dump(s,nnf)
    except EOFError:
        pass
    nf.close()
    nnf.close()
    os.remove("scard.dat")
    os.rename("s1.dat","scard.dat")
    return u

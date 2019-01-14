import pickle
import random
class lucky():
    def __init__(self,name,price,avail):
        self.product=name
        self.price=price
        self.avail=avail
    def __str__(self):
        return str(self.product)+','+str(self.price)+','+str(self.avail)
    
def disp():
    f1=open("lucky.dat","rb")
    try:
        while True:
            s=pickle.load(f1)
            print s
    except EOFError:
        pass
    f1.close()
def change(d,icode):
   f1=open("lucky.dat","ab")
   l=[]
   for i in d:
       if i==icode:
           x=d[icode]["Product"]
           y=d[icode]["Price"]
           z=d[icode]["Availability"]
           s=lucky(x,y,z)
           
           print d[icode]
           print "Are you sure you want to delete this item?"
           r=raw_input("Yes/No")
           if r.lower()=="yes":
               del d[icode]
               print "Deleted"
               pickle.dump(s,f1)
               break
           else:
               break
             
   f1.close() 
   return d
def draw():
    f1=open("lucky.dat","rb")
    l1=[]
    l2=[]
    l=[]
    try:
        while True:
            s=pickle.load(f1)
            a=[]
            a.extend([s.product,s.price,s.avail])
            l1.append(a)
    except EOFError:
        pass
    f1.close()
    for i in range (len(l1)):
        l2.append("")
    l=l1+l2
    
    random.shuffle(l)
    a=random.randint(0,len(l)-1)
    if l[a]=="":
        print "Sorry! Better luck next time!"
    else:
        print "Congrats! You have won a:",l[a][0]
        l[a][2]-=1
    f1=open("lucky.dat","wb")
    for i in l:
        if i!="":
            x=i[0]
            y=i[1]
            z=i[2]
            if z!=0:
                s=lucky(x,y,z)
                pickle.dump(s,f1)
            else:
                pass
    f1.close()

import pickle
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
    def print2(self):
        for i in self.d1:
            print i,self.d1[i]
    def print3(self):
        for i in self.d1:
            print i,self.d1[i]
    def print4(self):
        for i in self.d1:
            print i,self.d1[i]
    def print5(self):
        for i in self.d1:
            print i,self.d1[i]        
f1=open("cat.dat","wb")
d1={1:{"Product":"Ponds age miracle","Price":30,"Availability":25},2:{"Product":"Olay total effects","Price":62,"Availability":30},3:{"Product":"Nivea body lotion","Price":23,"Availability":20},4:{"Product":"Loreal paris shampoo","Price":56,"Availability":25},5:{"Product":"Vaseline petroleum jelly","Price":12,"Availability":30},6:{"Product":"Garnier colour naturals","Price":16,"Availability":12},7:{"Product":"Clean and clear makeup remover","Price":15,"Availability":10},8:{"Product":"Ponds white radiance","Price":22,"Availability":12},9:{"Product":"Parachute hair oil","Price":12,"Availability":12},10:{"Product":"Enchanteur body lotion","Price":21,"Availability":12},11:{"Product":"Lux soap","Price":5,"Availability":10},12:{"Product":"Lifebuoy body wash","Price":15,"Availability":9}}
           
d2={13:{"Product":"Samsung Galaxy Note 7 smartphone","Price":3250,"Availability":5},14:{"Product":"Samsung smart 3D HD tv, 40\"","Price":2999,"Availability":5},15:{"Product":"Sony Handicam","Price":399,"Availability":9},16:{"Product":"Dell inspiron laptap","Price":1999,"Availability":3},17:{"Product":"Bose home theatre","Price":12999,"Availability":3},18:{"Product":"HP All-in-one printer","Price":1699,"Availability":12},19:{"Product":"Nikon camera","Price":2999,"Availability":7},20:{"Product":"Lenovo Yoga Tab","Price":1999,"Availability":10},21:{"Product":"Bosch dishwasher","Price":2000,"Availability":5},22:{"Product":"Moulinex Food processor","Price":300,"Availability":4},23:{"Product":"Braun Hair Dryer","Price":50,"Availability":8},24:{"Product":"Iphone 8 64GB","Price":4400,"Availability":5}}

d3={25:{"Product":"Assorted pencil boxes","Price":8,"Availability":9},26:{"Product":"Highlighters","Price":2,"Availability":12},27:{"Product":"Assorted sharpners","Price":2,"Availability":15},28:{"Product":"Montex ink pen","Price":3,"Availability":8},29:{"Product":"Oval white ink","Price":3,"Availability":6},30:{"Product":"Flamingo stapler","Price":9,"Availability":10},31:{"Product":"Maped colour pencils 24","Price":20,"Availability":4},32:{"Product":"Faber castell water colours","Price":20,"Availability":5},33:{"Product":"Camlin ruler ","Price":2,"Availability":10},34:{"Product":"Sinarline 200pg ruled notebook","Price":3.50,"Availability":20},35:{"Product":"Excel Register 2QR","Price":8,"Availability":9},36:{"Product":"Cello ballpoint pen","Price":1,"Availability":30},37:{"Product":"Flamingo geometry box","Price":10,"Availability":10},38:{"Product":"Staedler pencil per packet","Price":5,"Availability":32},39:{"Product":"Apsara eraser per packet","Price":5,"Availability":25}}

d4={40:{"Product":"Girl's skirts","Price":15,"Availability":8},41:{"Product":"Socks 3pcs","Price":8,"Availability":20},42:{"Product":"Men's shirts","Price":35,"Availability":20},43:{"Product":"Ladies sweaters","Price":34,"Availability":12},44:{"Product":"Boy's pants","Price":30,"Availability":10},45:{"Product":"Girl's top assorted","Price":12,"Availability":20},46:{"Product":"Men's t-shirts assorted","Price":22,"Availability":13},47:{"Product":"Ladies trousers","Price":20,"Availability":6},48:{"Product":"Men's bermudas","Price":20,"Availability":9},49:{"Product":"Ladies dresses","Price":30,"Availability":10}}

d5={50:{"Product":"Dettol hand wash","Price":9,"Availability":10},51:{"Product":"Tide detergent","Price":25,"Availability":20},52:{"Product":"Clorax Disinfectant","Price":30,"Availability":10},53:{"Product":"Toilet paper rolls 2pcs","Price":10,"Availability":30},54:{"Product":"Bleach","Price":20,"Availability":10},55:{"Product":"Mop","Price":20,"Availability":5},56:{"Product":"Lux Dishwashing Liquid","Price":15,"Availability":10},57:{"Product":"Wiper","Price":13,"Availability":8},58:{"Product":"Loofah","Price":5,"Availability":9},59:{"Product":"Gilette shaving gel","Price":15,"Availability":10}}

d=caty(d1,d2,d3,d4,d5)

pickle.dump(d,f1)
f1.close()

from tkinter import *
from tkinter import ttk,messagebox
import mysql.connector as co

mycon = co.connect(host= "localhost", user = "root", passwd= "Joy06092006", database= "cms")
cursor = mycon.cursor()

sales=[]
sl=[]
sa=[]

aqua_screen = Tk()
aqua_screen.title("Aqua")
aqua_screen.geometry('1200x650')
aqua_screen.configure(bg="#57a1f8")
aqua_screen.resizable(False,False)

cursor.execute("CREATE TABLE IF NOT EXISTS luxurious_cars (ModelNumber INT PRIMARY KEY, ModelName VARCHAR(500), Price DECIMAL (10,2))")
cursor.execute("CREATE TABLE IF NOT EXISTS mpv_cars (ModelNumber INT PRIMARY KEY, ModelName VARCHAR(500), Price DECIMAL (10,2))")
cursor.execute("CREATE TABLE IF NOT EXISTS com_cars (ModelNumber INT PRIMARY KEY, ModelName VARCHAR(500), Price DECIMAL (10,2))")
cursor.execute("CREATE TABLE IF NOT EXISTS bikes (ModelNumber INT PRIMARY KEY, ModelName VARCHAR(500), Price DECIMAL (10,2))")
cursor.execute("CREATE TABLE IF NOT EXISTS sales (ModelNumber INT PRIMARY KEY, ModelName VARCHAR(500), Price DECIMAL (10,2), salenumber INT)")
cursor.execute("CREATE TABLE IF NOT EXISTS cardata (sellername VARCHAR(200), aadhar VARCHAR(200), price VARCHAR(200), carcon VARCHAR(200), modelname VARCHAR(500), bankno VARCHAR(200), contactno VARCHAR(100))")

'''sqlstatement1 = "INSERT INTO luxurious_cars VALUES (%s, %s, %s)"
val1 = [("110001", "Range Rover Velar", "9000000.00"),
       ("110002", "BMW X3", "7000000.00"),
       ("110003", "Mercedes Benz S Class", "32000000.00"),
       ("110004", "Rolls Royce Phantom", "9500000.00"),
       ("110005", "Audi Q7", "9300000.00"),
       ("110006", "Maruti", "200000.00")]
cursor.executemany(sqlstatement1, val1)
mycon.commit()

#adding values into com_cars table
sqlstatement2 = "INSERT INTO com_cars VALUES (%s, %s, %s)"
val2 = [("210001", "Hyundai Verna", "1500000.00"),
       ("210002", "Maruti Dzire", "900000.00"),
       ("210003", "Honda City", "1600000.00"),
       ("210004", "Tata Tigor", "800000.00"),
       ("210005", "Volkswagen Virtus", "1100000.00"),
       ("210006", "Hyundai Creta", "1900000.00"),
       ("210007", "Tata Harrier", "2700000.00"),
       ("210008", "Tata Nexon", "1600000.00"),
       ("210009", "Toyota Fortuner", "5100000.00"),
       ("210010", "Maruti Brezza", "1400000.00")]
cursor.executemany(sqlstatement2, val2)
mycon.commit()

#adding values into com_cars table
sqlstatement3 = "INSERT INTO mpv_cars VALUES (%s, %s, %s)"
val3 = [("310001", "Kia Carnival", "4000000.00"),
       ("310002", "Mahindra Marazzo", "1800000.00"),
       ("310003", "Toyota Rumion", "1600000.00"),
       ("310004", "Toyota Vellfire", "10000000.00"),
       ("310005", "Renault Triber", "800000.00"),
       ("310006", "Maruti Eeco", "500000.00"),
       ("310007", "Force Trax Cruiser", "1600000.00"),
       ("310008", "Toyota Fortuner", "5100000.00"),
       ("310009", "Maruti Ertiga", "1300000.00"),
       ("310010", "Toyota Innova", "2600000.00")]
cursor.executemany(sqlstatement3, val3)
mycon.commit()

#adding values into bikes table
sqlstatement4 = "INSERT INTO bikes VALUES (%s, %s, %s)"
val4 = [("410001", "Bajaj Pulsar RS200", "172000.00"),
       ("410002", "Bajaj Dominar 400", "230000.00"),
       ("410003", "Royal Enfield Classic", "193000.00"),
       ("410004", "Royal Enfield Himalayan", "216000.00"),
       ("410005", "Yamaha R15 V4", "200000.00"),
       ("410006", "Honda CB300R", "270000.00"),
       ("410007", "Hero Splendor Plus", "75000.00"),
       ("410008", "Honda Shine", "85000.00"),
       ("410009", "TVS Ntorq", "100000.00"),
       ("410010", "Honda Active 125", "85000.00")]
cursor.executemany(sqlstatement4, val4)
mycon.commit()

#adding sales list
sqlstatement5 = "INSERT INTO sales VALUES (%s, %s, %s, %s)"
val5 = [("110001", "Range Rover Velar", "9000000.00", "0"),
       ("110002", "BMW X3", "7000000.00", "0"),
       ("110003", "Mercedes Benz S Class", "32000000.00", "0"),
       ("110004", "Rolls Royce Phantom", "9500000.00", "0"),
       ("110005", "Audi Q7", "9300000.00", "0"),
       ("110006", "Maruti", "200000.00", "0"),
       ("210001", "Hyundai Verna", "1500000.00", "0"),
       ("210002", "Maruti Dzire", "900000.00", "0"),
       ("210003", "Honda City", "1600000.00", "0"),
       ("210004", "Tata Tigor", "800000.00", "0"),
       ("210005", "Volkswagen Virtus", "1100000.00", "0"),
       ("210006", "Hyundai Creta", "1900000.00", "0"),
       ("210007", "Tata Harrier", "2700000.00", "0"),
       ("210008", "Tata Nexon", "1600000.00", "0"),
       ("210009", "Toyota Fortuner", "5100000.00", "0"),
       ("210010", "Maruti Brezza", "1400000.00", "0"),
       ("310001", "Kia Carnival", "4000000.00", "0"),
       ("310002", "Mahindra Marazzo", "1800000.00", "0"),
       ("310003", "Toyota Rumion", "1600000.00", "0"),
       ("310004", "Toyota Vellfire", "10000000.00", "0"),
       ("310005", "Renault Triber", "800000.00", "0"),
       ("310006", "Maruti Eeco", "500000.00", "0"),
       ("310007", "Force Trax Cruiser", "1600000.00", "0"),
       ("310008", "Toyota Fortuner", "5100000.00", "0"),
       ("310009", "Maruti Ertiga", "1300000.00", "0"),
       ("310010", "Toyota Innova", "2600000.00", "0"),
       ("410001", "Bajaj Pulsar RS200", "172000.00", "0"),
       ("410002", "Bajaj Dominar 400", "230000.00", "0"),
       ("410003", "Royal Enfield Classic", "193000.00", "0"),
       ("410004", "Royal Enfield Himalayan", "216000.00", "0"),
       ("410005", "Yamaha R15 V4", "200000.00", "0"),
       ("410006", "Honda CB300R", "270000.00", "0"),
       ("410007", "Hero Splendor Plus", "75000.00", "0"),
       ("410008", "Honda Shine", "85000.00", "0"),
       ("410009", "TVS Ntorq", "100000.00", "0"),
       ("410010", "Honda Active 125", "85000.00", "0")]
cursor.executemany(sqlstatement5, val5)
mycon.commit()'''
#VARIABLES================================================================================================== 
number1=""
name1=""
price1=""

number2=""
name2=""
price2=""
totalprice=0
img= PhotoImage(file=r"C:\Users\joyde\Documents\python projects\car management\images\login.png")
imag1 = PhotoImage(file=r"C:\Users\joyde\Documents\python projects\car management\images\home.png")
imag2 = PhotoImage(file=r"C:\Users\joyde\Documents\python projects\car management\images\shop.png")
imag3 = PhotoImage(file=r"C:\Users\joyde\Documents\python projects\car management\images\home.png")
imag4 = PhotoImage(file=r"C:\Users\joyde\Documents\python projects\car management\images\setting.png")
imag5 = PhotoImage(file=r"C:\Users\joyde\Documents\python projects\car management\images\logout.png")
l1 = PhotoImage(file=r"C:\Users\joyde\Documents\python projects\car management\images\lr.png")
l2 = PhotoImage(file=r"C:\Users\joyde\Documents\python projects\car management\images\bmw.png")
l3 = PhotoImage(file=r"C:\Users\joyde\Documents\python projects\car management\images\mb.png")
l4 = PhotoImage(file=r"C:\Users\joyde\Documents\python projects\car management\images\rr.png")
l5 = PhotoImage(file=r"C:\Users\joyde\Documents\python projects\car management\images\audi.png")
l6 = PhotoImage(file=r"C:\Users\joyde\Documents\python projects\car management\images\minicooper.png")
c1 = PhotoImage(file=r"C:\Users\joyde\Documents\python projects\car management\images\verna.png")
c2 = PhotoImage(file=r"C:\Users\joyde\Documents\python projects\car management\images\dzire.png")
c3 = PhotoImage(file=r"C:\Users\joyde\Documents\python projects\car management\images\city.png")
c4 = PhotoImage(file=r"C:\Users\joyde\Documents\python projects\car management\images\tigor.png")
c5 = PhotoImage(file=r"C:\Users\joyde\Documents\python projects\car management\images\virtus.png")
c6 = PhotoImage(file=r"C:\Users\joyde\Documents\python projects\car management\images\creta.png")
c7 = PhotoImage(file=r"C:\Users\joyde\Documents\python projects\car management\images\harrier.png")
c8 = PhotoImage(file=r"C:\Users\joyde\Documents\python projects\car management\images\nexon.png")
c9 = PhotoImage(file=r"C:\Users\joyde\Documents\python projects\car management\images\fortuner.png")
c10 = PhotoImage(file=r"C:\Users\joyde\Documents\python projects\car management\images\brezza.png")
m1 = PhotoImage(file=r"C:\Users\joyde\Documents\python projects\car management\images\carnival.png")
m2 = PhotoImage(file=r"C:\Users\joyde\Documents\python projects\car management\images\marazzo.png")
m3 = PhotoImage(file=r"C:\Users\joyde\Documents\python projects\car management\images\rumion.png")
m4 = PhotoImage(file=r"C:\Users\joyde\Documents\python projects\car management\images\vellfire.png")
m5 = PhotoImage(file=r"C:\Users\joyde\Documents\python projects\car management\images\triber.png")
m6 = PhotoImage(file=r"C:\Users\joyde\Documents\python projects\car management\images\eeco.png")
m7 = PhotoImage(file=r"C:\Users\joyde\Documents\python projects\car management\images\trax.png")
m8 = PhotoImage(file=r"C:\Users\joyde\Documents\python projects\car management\images\fortuner.png")
m9 = PhotoImage(file=r"C:\Users\joyde\Documents\python projects\car management\images\ertiga.png")
m10 = PhotoImage(file=r"C:\Users\joyde\Documents\python projects\car management\images\innova.png")
b1 = PhotoImage(file=r"C:\Users\joyde\Documents\python projects\car management\images\rs200.png")
b2 = PhotoImage(file=r"C:\Users\joyde\Documents\python projects\car management\images\dominar400.png")
b3 = PhotoImage(file=r"C:\Users\joyde\Documents\python projects\car management\images\classic.png")
b4 = PhotoImage(file=r"C:\Users\joyde\Documents\python projects\car management\images\himalayan.png")
b5 = PhotoImage(file=r"C:\Users\joyde\Documents\python projects\car management\images\r15.png")
b6 = PhotoImage(file=r"C:\Users\joyde\Documents\python projects\car management\images\cb400r.png")
b7 = PhotoImage(file=r"C:\Users\joyde\Documents\python projects\car management\images\plus.png")
b8 = PhotoImage(file=r"C:\Users\joyde\Documents\python projects\car management\images\shine.png")
b9 = PhotoImage(file=r"C:\Users\joyde\Documents\python projects\car management\images\ntorq.png")
b10 = PhotoImage(file=r"C:\Users\joyde\Documents\python projects\car management\images\activa125.png")

def lux():
    global t
    t= 'l'
def com():
    global t
    t= 'c'
def mpv():
    global t
    t= 'm'
def bikes():
    global t
    t= 'b'
def allv():
    global t
    t = 'a' 

x=0
r=0
cart=0
cartlist=[]
buycar1=0
buycar2=0
buycarname=""
buycarprice=""

bg_color="#57a1f8"
seller_name=StringVar()
seller_aadhar=StringVar()
seller_price=StringVar()
seller_modelname=StringVar()
seller_bankno=StringVar()
seller_contactno=StringVar()
seller_desc=StringVar()
seller_condition=StringVar()
passwd=StringVar()
userid=StringVar()
passwd2=StringVar()
username=StringVar()
#to clear frame================================================================================
def clear(framename):
    for widgets in framename.winfo_children():
        widgets.destroy()
def close():
    aqua_screen.destroy()

#==============================================================================================-
def main():
    global number1
    global name1
    global price1
    
    global imag1
    global imag2
    global imag3
    global imag4
    global imag5
    
    global number2
    global name2
    global price2

    global x
    global buycar1
    global buycar2
    
    f1=Frame(aqua_screen,width=1150,height=600,bg='white')
    f1.place(x=26,y=26)

    L1=Frame(f1,width=1140,height=2,bg='black')
    L1.place(x=5,y=60)

    f2=Frame(f1,width=1000,height=500,bg='#57a1f8')
    f2.place(x=130,y=80)

    welcometxt=Label(f1,text="WELCOME TO THE AQUA",fg='black',bg='white',font=("Arial Bold",20))
    welcometxt.place(x=400,y=15)
#===============================================================================================

#categories=====================================================================================

#luxurious cars
    imag6 = PhotoImage(file=r"C:\Users\joyde\Documents\python projects\car management\images\luxcars2.png")
    def lux_cars():
        #clear_frame()
        ff1=Frame(f2,width=400,height=200,bg='white')
        ff1.place(x=70,y=30)

        lux_carname=Label(f2, text="Luxurious Cars", font=('Arial',15, 'bold'), fg='black', bg= "#57a1f8")
        lux_carname.place(x=190,y=235)
        
        lux_btn = Button(ff1, width=400, bd=0, height=200, bg='white',cursor="hand2",fg='black',image=imag6,command=lambda: [clear(f2),list1(),lux(),work(), shop1(),shop2(),nextbtn()])
        lux_btn.place(x=0,y=0)
    def list1():
        global l
        data1= " SELECT ModelNumber,ModelName,Price FROM luxurious_cars ;"
        cursor.execute(data1)
        data1f=cursor.fetchall()
        l= data1f
        #print(data1f)


#commercial cars
    imag7 = PhotoImage(file=r"C:\Users\joyde\Documents\python projects\car management\images\comcars2.png")
    def mpv_cars():
    
        ff2=Frame(f2,width=400,height=200,bg='white')
        ff2.place(x=530,y=30)

        mpv_carname=Label(f2, text="Affordable Cars", font=('Arial',15, 'bold'), fg='black', bg= "#57a1f8")
        mpv_carname.place(x=650,y=235)
        
        mpv_btn = Button(ff2, width=400, bd=0, height=200, bg='white',cursor="hand2",fg='black',image=imag7,command=lambda: [clear(f2),mpv(),list2(),work(), shop1(),shop2(),nextbtn()])
        mpv_btn.place(x=0,y=0)
    def list2():
        global l 
        data2= " SELECT ModelNumber,ModelName,Price FROM mpv_cars ;"
        cursor.execute(data2)
        data2f=cursor.fetchall()
        l=data2f
        #print(data2f)

#commercial cars
    imag8 = PhotoImage(file=r"C:\Users\joyde\Documents\python projects\car management\images\affcars2.png")
    def com_cars():

        ff3=Frame(f2,width=400,height=200,bg='white')
        ff3.place(x=70,y=270)

        com_carname=Label(f2, text="Commercial Cars", font=('Arial',15, 'bold'), fg='black', bg= "#57a1f8")
        com_carname.place(x=190,y=470)
        
        com_btn = Button(ff3, width=400, bd=0, height=200, bg='white',cursor="hand2",fg='black',image=imag8,command=lambda: [clear(f2),com(),list3(),work(), shop1(),shop2(),nextbtn()])
        com_btn.place(x=0,y=0)
    def list3():
        global l 
        data3= " SELECT ModelNumber,ModelName,Price FROM com_cars ;"
        cursor.execute(data3)
        data3f=cursor.fetchall()
        l=data3f
       # print(data3f)

#two wheelers
    imag9 = PhotoImage(file=r"C:\Users\joyde\Documents\python projects\car management\images\twowheel.png")
    def twowheel():
    
        ff4=Frame(f2,width=400,height=200,bg='white')
        ff4.place(x=530,y=270)

        bikes_carname=Label(f2, text="Two Wheelers", font=('Arial',15, 'bold'), fg='black', bg= "#57a1f8")
        bikes_carname.place(x=650,y=470)
    
        twowheel_btn = Button(ff4, width=400, bd=0, height=200, bg='white',cursor="hand2",fg='black',image=imag9,command=lambda: [clear(f2),bikes(),list4(),work(), shop1(),shop2(),nextbtn()])
        twowheel_btn.place(x=0,y=0)
    def list4():
        global l
        data4= " SELECT ModelNumber,ModelName,Price FROM bikes ;"
        cursor.execute(data4)
        data4f=cursor.fetchall()
        l= data4f
       # print(data4f)

#shopping menu=======================================================================================

    def shop1():
        
        global number1
        global name1
        global price1
    
        fs1=Frame(f2,width=400,height=380,bg='white')
        fs1.place(x=70,y=30)

        txtmnumber1=Label(fs1,text="Model No:",fg='black',bg='white',font=("Arial Bold",15))
        txtmnumber1.place(x=30,y=240)

        txtmname1=Label(fs1,text="Model Name:",fg='black',bg='white',font=("Arial Bold",15))
        txtmname1.place(x=30,y=280)

        txtprice1=Label(fs1,text="Price:",fg='black',bg='white',font=("Arial Bold",15))
        txtprice1.place(x=30,y=320)
    
        mnumber1=Label(fs1,text=number1, fg='black', bg='white', font=("Arial",15))
        mnumber1.place(x=170,y=240)

        mname1=Label(fs1,text=name1, fg='black', bg='white', font=("Arial",15))
        mname1.place(x=170,y=280)

        mprice1=Label(fs1,text=price1, fg='black', bg='white', font=("Arial",15))
        mprice1.place(x=170,y=320)
    
        buy_btn1 = Button(f2, text= "BUY NOW", height=3,width=25, bd=0, bg='blue',cursor="hand2",fg='white', font=("Arial bold",9), command= buynow1)
        buy_btn1.place(x=70,y=420)

        cart_btn1 = Button(f2, text= "DETAILS", height=3,width=25, bd=0, bg='navy blue',cursor="hand2",fg='white', font=("Arial bold",9))
        cart_btn1.place(x=288,y=420)

        def pic1():
            if t=='l':
                if x==0:
                    im= l1
                elif x==2:
                    im= l3
                else:
                    im= l5
            elif t=='m':
                if x==0:
                    im= m1
                elif x==2:
                    im= m3
                elif x==4:
                    im= m5
                elif x== 6:
                    im = m7
                else:
                    im = m9
            elif t=='c':
                if x==0:
                    im= c1
                elif x==2:
                    im= c3
                elif x==4:
                    im= c5
                elif x== 6:
                    im = c7
                else:
                    im = c9
            elif t=='b':
                if x==0:
                    im= b1
                elif x==2:
                    im= b3
                elif x==4:
                    im= b5
                elif x== 6:
                    im = b7
                else:
                    im = b9
            elif t=='a':
                if x==0:
                    im = l1
                elif x== 2:
                    im= l3
                elif x== 4:
                    im = l5
                elif x== 6:
                    im = m1
                elif x== 8:
                    im = m3
                elif x== 10:
                    im = m5
                elif x== 12:
                    im = m7
                elif x== 14:
                    im = m9
                elif x== 16:
                    im = c1
                elif x == 18:
                    im = c3
                elif x == 20:
                    im = c5
                elif x == 22:
                    im = c7
                elif x == 24:
                    im = c9
                elif x == 26:
                    im= b1
                elif x == 28:
                    im = b3
                elif x == 30:
                    im = b5
                elif x == 32:
                    im = b7
                else:
                    im = b9
                
            pic1= Button(fs1, width= 350, bd=0, height= 170,bg='white', cursor="hand2", fg='black',image=im)
            pic1.place(x=25, y=35 )
        pic1()

      
        

    def shop2():
        global number2
        global name2
        global price2
    
        fs2=Frame(f2,width=400,height=380,bg='white')
        fs2.place(x=530,y=30)
        txtmnumber2=Label(fs2,text="Model No:",fg='black',bg='white',font=("Arial Bold",15))
        txtmnumber2.place(x=30,y=240)

        txtmname2=Label(fs2,text="Model Name:",fg='black',bg='white',font=("Arial Bold",15))
        txtmname2.place(x=30,y=280)

        txtprice2=Label(fs2,text="Price:",fg='black',bg='white',font=("Arial Bold",15))
        txtprice2.place(x=30,y=320)

        nextbtn()

        mnumber2=Label(fs2,text=number2, fg='black', bg='white', font=("Arial",15))
        mnumber2.place(x=170,y=240)

        mname2=Label(fs2,text=name2, fg='black', bg='white', font=("Arial",15))
        mname2.place(x=170,y=280)

        mprice2=Label(fs2,text=price2, fg='black', bg='white', font=("Arial",15))
        mprice2.place(x=170,y=320)

        buy_btn2 = Button(f2, text= "BUY NOW", height=3,width=25, bd=0, bg='blue',cursor="hand2",fg='white', font=("Arial bold",9), command= buynow2)
        buy_btn2.place(x=530,y=420)

        cart_btn2 = Button(f2, text= "DETAILS", height=3,width=25, bd=0, bg='navy blue',cursor="hand2",fg='white', font=("Arial bold",9))
        cart_btn2.place(x=748,y=420)

        def pic2():
            if t== 'l':
                if x== 0:
                    im=l2
                elif x==2:
                    im= l4
                else:
                    im= l6
            elif t=='m':
                if x== 0:
                    im=m2
                elif x==2:
                    im= m4
                elif x==4:
                    im= m6
                elif x==6:
                    im= m8
                else:
                    im= m10
            elif t=='c':
                if x== 0:
                    im=c2
                elif x==2:
                    im= c4
                elif x==4:
                    im= c6
                elif x==6:
                    im= c8
                else:
                    im= c10
            elif t=='b':
                if x== 0:
                    im=b2
                elif x==2:
                    im= b4
                elif x==4:
                    im= b6
                elif x==6:
                    im= b8
                else:
                    im= b10
            elif t=='a':
                if x==0:
                    im = l2
                elif x== 2:
                    im= l4
                elif x== 4:
                    im = l6
                elif x== 6:
                    im = m2
                elif x== 8:
                    im = m4
                elif r== 10:
                    im = m6
                elif x== 12:
                    im = m8
                elif x== 14:
                    im = m10
                elif x== 16:
                    im = c2
                elif x == 18:
                    im = c4
                elif x == 20:
                    im = c6
                elif x == 22:
                    im = c8
                elif x == 24:
                    im = c10
                elif x == 26:
                    im= b2
                elif x == 28:
                    im = b4
                elif x == 30:
                    im = b6
                elif x == 32:
                    im = b8
                else:
                    im = b10
                    
                    
                
            pic2= Button(fs2, width= 350, bd=0, height= 170,bg='white', cursor="hand2", fg='black',image=im)
            pic2.place(x=25, y=35 )
        pic2()

        
        
    def nextbtn():
        nextbtn= Button(f2,text= ">>",height=3,width=5, bd=0, bg='navy blue',cursor="hand2",fg='white',font=("Arial bold",10), command= lambda: [clear(f2), shop1(), shop2(), sync(), work()] )
        nextbtn.place(x=944,y=200)
        #print(x)

    def sync():
        global x
        x=x+2

    def work():
        c=0
        d=0
        global x
        global number1
        global name1
        global price1

        global number2
        global name2
        global price2
    
        while d<len(l)and c<len(l):
            nextbtn()

            number1=l[c][0]
            name1=l[c][1]
            price1=l[c][2]

            number2=l[c+1][0]
            name2=l[c+1][1]
            price2=l[c+1][2]
            if x!=0:
                c=x
                if c==len(l):
                    x=0
            shop1()
            shop2()
            d=d+1

    def buynow1():
        global x
        global buycar1
        global buycarname
        global buycarprice
        buycar1= l[x][0]
        buycarname= l[x][1]
        buycarprice= l[x][2]
        clear(aqua_screen)
        billingbuy()

    
    def buynow2():
        global x
        global buycar1
        buycar1= l[x+1][0]
        global buycarname
        global buycarprice
        buycar1= l[x+1][0]
        buycarname= l[x+1][1]
        buycarprice= l[x+1][2]
        clear(aqua_screen)
        billingbuy()
        
        
            
#selling=============================================================================================
    def sell():
        global passwd
        f3=Frame(f2,width=970,height=470,bg='white')
        f3.place(x=15,y=15)
        global img

        pic = Label(f3,image=img,bg='white')
        pic.place(x=50,y=50)

        frame=Frame(f3,width=350,height=350,bg='white')
        frame.place(x=480,y=70)
        
        heading=Label(frame,text="Sell Now",fg='#57a1f8',bg='white',font=("Microsoft YaHei UI Light",23,'bold'))
        heading.place(x=100,y=5)

        #-------------------------------------------------------------------------------

        def on_enter(e):
            user.delete(0,'end')

        def on_leave(e):
            name=user.get()
            if name=='':
                user.insert(0, 'UserID')
        
        user = Entry(frame,width=25,fg='black',border=0,bg='white',font=("Microsoft YaHei UI Light",11),textvariable=userid)
        user.place(x=30,y=80)
        user.insert(0,'UserID')
        user.bind("<FocusIn>", on_enter)
        user.bind("<FocusOut>", on_leave)

        frame2=Frame(frame,width=295,height=2,bg='black')
        frame2.place(x=25,y=107)

    #-------------------------------------------------------------------------------
        def on_enter(e):
            password.delete(0,'end')

        def on_leave(e):
            name=password.get()
            if name=='':
                password.insert(0, 'Password')
        
        password = Entry(frame,width=25,fg='black',border=0,bg='white',font=("Microsoft YaHei UI Light",11),textvariable=passwd,show='*')
        password.place(x=30,y=150)
        password.insert(0,'Password')
        password.bind("<FocusIn>", on_enter)
        password.bind("<FocusOut>", on_leave)


        frame3=Frame(frame,width=295,height=2,bg='black')
        frame3.place(x=25,y=177)

    #-------------------------------------------------------------------------------
        def sellcheck():
            if userid.get()=='' or passwd.get()=='':
                messagebox.showerror('Error','All fields are required ?')
            else:
                if passwd.get()=="12345":
                    sellscreen()
                else:
                    messagebox.showerror("Access Denied","Contact the developer to get the password")
                
        sell_btn=Button(frame,width=39,pady=7,text='Sell Now',bg='#57a1f8',fg='white',cursor="hand2",border=0,command=sellcheck)
        sell_btn.place(x=35,y=204)


#side buttons========================================================================================

#homebtn
    f3=Frame(f1,width=105,height=90,bg='white', bd=5, relief=RAISED)
    f3.place(x=13,y=80)

    home_btn = Button(f3, bd=0, bg='white',cursor="hand2",fg='black',image=imag1)
    home_btn.place(x=23,y=0)

    home_btn1 = Button(f3,width=6,text='HOME',bd=0, bg='white',cursor="hand2",fg='black',font=("Arial Bold",11), command=lambda: [clear(f2),lux_cars(),com_cars(),twowheel(),mpv_cars()])
    home_btn1.place(x=18,y=48)



#shoppingbtn
    f4=Frame(f1,width=105,height=90,bg='white', bd=5, relief=RAISED)
    f4.place(x=13,y=183)

    shop_btn = Button(f4, bd=0, bg='white',cursor="hand2",fg='black',image=imag2)
    shop_btn.place(x=23,y=0)

    shop_btn1 = Button(f4,width=6,text='SHOP',bd=0, bg='white',cursor="hand2",fg='black',font=("Arial Bold",11),command=lambda: [clear(f2),all_list(),allv(),work(), shop1(),shop2(),nextbtn()])
    shop_btn1.place(x=18,y=48)

    def all_list():
        global l
        global sl
        dataA= " SELECT ModelNumber,ModelName,Price FROM luxurious_cars;"
        cursor.execute(dataA)
        dataAf=cursor.fetchall()
        
        dataA1= " SELECT ModelNumber,ModelName,Price FROM mpv_cars;"
        cursor.execute(dataA1)
        dataA1f=cursor.fetchall()
        
        dataA2= " SELECT ModelNumber,ModelName,Price FROM com_cars;"
        cursor.execute(dataA2)
        dataA2f=cursor.fetchall()
        
        dataA3= " SELECT ModelNumber,ModelName,Price FROM bikes;"
        cursor.execute(dataA3)
        dataA3f=cursor.fetchall()
        
        l= dataAf + dataA1f + dataA2f + dataA3f
        sl=l


#sellbtn
    f5=Frame(f1,width=105,height=90,bg='white', bd=5, relief=RAISED)
    f5.place(x=13,y=285)

    sell_btn = Button(f5, bd=0, bg='white',cursor="hand2",fg='black',image=imag3)
    sell_btn.place(x=23,y=0)

    sell_btn1 = Button(f5,width=6,text='SELL',bd=0, bg='white',cursor="hand2",fg='black',font=("Arial Bold",11), command=lambda: [clear(f2),sell()])
    sell_btn1.place(x=18,y=48)


#settingbtn
    f6=Frame(f1,width=105,height=90,bg='white', bd=5, relief=RAISED)
    f6.place(x=13,y=387)

    setting_btn = Button(f6, bd=0, bg='white',cursor="hand2",fg='black',image=imag4)
    setting_btn.place(x=23,y=0)

    setting_btn1 = Button(f6,width=7,text='SETTING',bd=0, bg='white',cursor="hand2",fg='black',font=("Arial Bold",11),command=settingscreen)
    setting_btn1.place(x=16,y=48)


#logoutbtn
    f7=Frame(f1,width=105,height=90,bg='white', bd=5, relief=RAISED)
    f7.place(x=13,y=490)

    lgout_btn = Button(f7, bd=0, bg='white',cursor="hand2",fg='black',image=imag5)
    lgout_btn.place(x=23,y=0)

    lgout_btn1 = Button(f7,width=6,text='EXIT',bd=0, bg='white',cursor="hand2",fg='black',font=("Arial Bold",11),command=close)
    lgout_btn1.place(x=18,y=48)

    lux_cars()
    com_cars()
    twowheel()
    mpv_cars()

    
    
#================================================================================================================================
def salesfn():
        global sales
        global sl
        global totalprice
        data= " SELECT * FROM sales ORDER BY salenumber DESC;"
        cursor.execute(data)
        sl=cursor.fetchall()
        c=0
        while c<len(sl):
            if sl[c][3]==0:
                totalprice= totalprice + sl[c][2]
            else:
                totalprice= totalprice + sl[c][2]*sl[c][3]
            c=c+1

def billingbuy():
    cess=0.0
    gst=0.0
    
    #max=90000000000.00
    global x
    global buycar1
    global buycar2
    global buycarname
    global buycarprice
    
    delfee = "300"
    cesscar=float(buycarprice)*(0.03)
    gstcar=float(buycarprice)*(0.18)
    roadtax1=6250.00
    
    bg_color= "#57a1f8"
    totalint=0
    totalstr=""
    totalintcar= float(buycarprice) + float(delfee) + float(gstcar) + float(roadtax1) + float(cesscar)
    totalstrcar= str(totalintcar)
    
    def receipt():
        
        textarea.delete(1.0,END)
        textarea.insert(END,f' Model \t Products \t     Price of Products\n')
        textarea.insert(END,f'\n Car\t  {buycar1}\t           {buycarprice}')
        textarea.insert(END,f'\n Tax\t  GST\t           {gstcar}')
        textarea.insert(END,f'\n Tax\t  Road Tax\t          {roadtax1}')
        textarea.insert(END,f'\n Tax\t  CESS\t            {cesscar}')
        textarea.insert(END,f"\n\n==================================")
        textarea.insert(END,f'\n Total : \t\t         {totalstrcar}')
        textarea.insert(END,f"\n==================================")
        
    def cancel():
        if messagebox.askyesno('Cancel','Do you really want to cancel transaction'):
            clear(aqua_screen)
            main()
    
    def exit():
        if messagebox.askyesno('Exit','Do you really want to exit'):
            aqua_screen.destroy()

    def finalbuy():
        global sales
        global buycar1
        buycar = int(buycar1)
        if messagebox.askyesno('Proceed','Do you want to proceed transaction'):
            data= " SELECT ModelName, Price, salenumber FROM sales WHERE ModelNumber = %s;"
            val= (buycar,)
            cursor.execute(data, val)
            dataa=cursor.fetchall()
            sales=dataa
            add = 1 + sales[0][2]
            sqll = "UPDATE sales SET salenumber = %s WHERE ModelNumber = %s"
            vall = (add,buycar)
            cursor.execute(sqll, vall)
            mycon.commit()
            clear(aqua_screen)
            main()
            messagebox.showinfo("Confirmation", " You Have successfully purchased a car")

    #heading name
    billhead=Label(aqua_screen,pady=5,text="Transaction",bd=12,bg=bg_color,fg='white',font=('Arial Bold', 35 ,'bold'),relief=GROOVE,justify=CENTER)
    billhead.pack(fill=X)

    #productdetails frame
    billframe1 = LabelFrame(aqua_screen, text='Product Details', font=('Arial', 18, 'bold'), fg='white',bg=bg_color,bd=15,relief=RIDGE)
    billframe1.place(x=5, y=90,width=800,height=450)

    #productdetails heading
    mnumberbill=Label(billframe1, text='Model No', font=('Helvetic',15, 'bold','underline'), fg='black',bg=bg_color)
    mnumberbill.grid(row=0,column=0,padx=20,pady=15)

    mnamebill=Label(billframe1, text='Products', font=('Helvetic',15, 'bold','underline'), fg='black',bg=bg_color)
    mnamebill.grid(row=0,column=1,padx=60,pady=15)

    mpricebill=Label(billframe1, text='Price (Rupees)', font=('Helvetic',15, 'bold','underline'), fg='black',bg=bg_color)
    mpricebill.grid(row=0,column=2,padx=30,pady=15)

    deliverybill=Label(billframe1, text='Delivery Fee', font=('Helvetic',15, 'bold','underline'), fg='black',bg=bg_color)
    deliverybill.grid(row=0,column=3,padx=30,pady=15)



    #productdetails products
    carnumber=Label(billframe1, text=buycar1, font=('Arial',15, 'bold'), fg='black',bg=bg_color)
    carnumber.grid(row=1,column=0,padx=20,pady=15)
    
    carname=Label(billframe1, text=buycarname, font=('Arial',15, 'bold'), fg='black',bg=bg_color)
    carname.grid(row=1,column=1,padx=20,pady=15)
    
    carprice=Label(billframe1, text=buycarprice, font=('Arial',15, 'bold'), fg='black',bg=bg_color)
    carprice.grid(row=1,column=2,padx=20,pady=15)
    
    delcarprice=Label(billframe1, text=delfee, font=('Arial',15, 'bold'), fg='black',bg=bg_color)
    delcarprice.grid(row=1,column=3,padx=20,pady=15)

    space1=Label(billframe1, text=buycar1, font=('Arial',15, 'bold'), fg='black',bg=bg_color)
    space1.grid(row=2,column=0,padx=20,pady=15)

    gst1=Label(billframe1, text='GST', font=('Arial',15, 'bold'), fg='black',bg=bg_color)
    gst1.grid(row=2,column=1,padx=20,pady=15)

    gstprice=Label(billframe1, text=gstcar, font=('Arial',15, 'bold'), fg='black',bg=bg_color)
    gstprice.grid(row=2,column=2,padx=20,pady=15)
    
    space2=Label(billframe1, text=buycar1, font=('Arial',15, 'bold'), fg='black',bg=bg_color)
    space2.grid(row=3,column=0,padx=20,pady=15)

    tax1=Label(billframe1, text='Road Tax', font=('Arial',15, 'bold'), fg='black',bg=bg_color)
    tax1.grid(row=3,column=1,padx=20,pady=15)
    
    roadtax=Label(billframe1, text=roadtax1, font=('Arial',15, 'bold'), fg='black',bg=bg_color)
    roadtax.grid(row=3,column=2,padx=20,pady=15)
    
    space3=Label(billframe1, text=buycar1, font=('Arial',15, 'bold'), fg='black',bg=bg_color)
    space3.grid(row=4,column=0,padx=20,pady=15)

    tax2=Label(billframe1, text='CESS', font=('Arial',15, 'bold'), fg='black',bg=bg_color)
    tax2.grid(row=4,column=1,padx=20,pady=15)
    
    roadtax=Label(billframe1, text=cesscar, font=('Arial',15, 'bold'), fg='black',bg=bg_color)
    roadtax.grid(row=4,column=2,padx=20,pady=15)

    def total():

        totallabel=Label(billframe1, text='Total : ', font=('Arial',15, 'bold'), fg='black',bg=bg_color)
        totallabel.grid(row=5,column=0,padx=20,pady=15)

        totalprice=Label(billframe1, text=totalstrcar, font=('Arial',15, 'bold'), fg='black',bg=bg_color)
        totalprice.grid(row=5,column=2,padx=20,pady=15)
    
        totalvalue=Label(billframe1, text=totalstr, font=('Arial',15, 'bold'), fg='black',bg=bg_color)
        totalvalue.grid(row=5,column=3,padx=20,pady=15)

    #butoons
    F3 =Frame(aqua_screen,bg=bg_color,bd=15,relief=RIDGE)
    F3.place(x=5, y=530,width=1200,height=120)

    buynowbtn = Button(F3, text='BUY', font='arial 20 bold', padx=5, pady=5, bg='navy blue',fg='white',width=10, cursor="hand2", command=finalbuy)
    buynowbtn.grid(row=0,column=0,padx=20,pady=10)

    totalbtn = Button(F3, text='TOTAL', font='arial 20 bold', padx=5, pady=5, bg='blue',fg='white',width=10, command=total, cursor="hand2")
    totalbtn.grid(row=0,column=1,padx=20,pady=10)

    receiptbtn = Button(F3, text='RECEIPT', font='arial 20 bold', padx=5, pady=5, bg='blue',fg='white',width=10,command=receipt, cursor="hand2")
    receiptbtn.grid(row=0,column=2,padx=20,pady=10)

    resetbtn = Button(F3, text='CANCEL', font='arial 20 bold', padx=5, pady=5, bg='blue',fg='white',width=10, command=cancel, cursor="hand2")
    resetbtn.grid(row=0,column=3,padx=20,pady=10)

    exitbtn = Button(F3, text='EXIT', font='arial 20 bold', padx=5, pady=5, bg='blue',fg='white',width=10, command=exit, cursor="hand2")
    exitbtn.grid(row=0,column=4,padx=20,pady=10)

    #billingview
    F2=Frame(aqua_screen,relief=GROOVE,bd=10)
    F2.place(x=800,y=90,width=400,height=440)
    bill_title=Label(F2,text='Receipt',font='arial 15 bold',bd=7,relief=GROOVE).pack(fill=X)
    textarea=Text(F2,font='arial 14')
    textarea.pack(fill=BOTH)
    
def sellscreen():
    clear(aqua_screen)
    global bg_color
    global seller_name
    global seller_aadhar
    global seller_price
    global seller_modelname
    global seller_bankno
    global seller_contactno
    global seller_desc
    global seller_condition
    
    #function===========================================================================================
    
    def add():
        if seller_name.get()=='' or seller_aadhar.get()=='' or seller_price.get()=='' or seller_condition.get()=='' or seller_modelname.get()=='' or seller_bankno.get()=='' or seller_contactno.get()=='':
            messagebox.showerror('Error','All fields are required ?')
        else:
            textarea.delete(1.0,END)
            textarea.insert(END, '\n=================================================')
            textarea.insert(END,f'\nModel Name:\t\t\t\t{seller_modelname.get()}')
            textarea.insert(END, '\n=================================================')
            textarea.insert(END, f'\n\nSeller Name:\t\t\t\t{seller_name.get()}')
            textarea.insert(END, f'\nAadhar:\t\t\t\t{seller_aadhar.get()}')
            textarea.insert(END, f'\nCondition:\t\t\t\t{seller_condition.get()}')
            textarea.insert(END, f'\nPrice:\t\t\t\t{seller_price.get()}')
            textarea.insert(END, f'\nBank No:\t\t\t\t{seller_bankno.get()}')
            textarea.insert(END, f'\nContact No:\t\t\t\t{seller_contactno.get()}')
            textarea.insert(END, f'\nDescription\t\t\t\t{sellerdesc.get(1.0, END)}')
            textarea.insert(END, '\n\n#################################################')

    def save():
        if seller_name.get()=='' or seller_aadhar.get()=='' or seller_price.get()=='' or seller_condition.get()=='' or seller_modelname.get()=='' or seller_bankno.get()=='' or seller_contactno.get()=='':
            messagebox.showerror('Error','All fields are required ?')
        else:
            cursor.execute(f"INSERT INTO cardata (sellername,aadhar,price,carcon,modelname,bankno,contactno) VALUES ('{seller_name.get()}','{seller_aadhar.get()}','{seller_price.get()}','{seller_condition.get()}','{seller_modelname.get()}','{seller_bankno.get()}','{seller_contactno.get()}')")
            mycon.commit()
            messagebox.showinfo("Review Confirmation","Your Car has been sent for review")
        
    def reset():
        textarea.delete(1.0,END)
        sellerdesc.delete(1.0,END)
        seller_name.set('')
        seller_aadhar.set('')
        seller_condition.set('')
        seller_modelname.set('')
        seller_price.set('')
        seller_bankno.set('')
        seller_contactno.set('')

    def cancel():
        if messagebox.askyesno('Cancel','Do you really want to cancel transaction'):
            clear(aqua_screen)
            main()
    
    def exit():
        if messagebox.askyesno('Exit','Do you really want to exit'):
            aqua_screen.destroy()
    
    #=====================Heading=======================
    title=Label(aqua_screen,text='Sell Your Car Now',bg=bg_color,fg='white',font=('Arial Bold',35,'bold'),relief=GROOVE,bd=12)
    title.pack(fill=X)

    #====================left frame details===================
    S1=Frame(aqua_screen,bg=bg_color,relief=RIDGE,bd=15)
    S1.place(x=8,y=80,width=650,height=475)

    sellername=Label(S1,text='Seller name :',font=('Arial Bold',15,'bold'),fg='black',bg=bg_color)
    sellername.grid(row=0,column=0,padx=30,pady=10)
    sellername=Entry(S1,font=('Arial Bold',12,'bold'),relief=RIDGE,bd=5, width=40, textvariable=seller_name)
    sellername.grid(row=0,column=1,pady=10)
    
    selleraadhar=Label(S1,text='Seller Aadhar :',font=('Arial Bold',15,'bold'),fg='black',bg=bg_color)
    selleraadhar.grid(row=1,column=0,padx=30,pady=10)
    selleraadhar=Entry(S1,font=('Arial Bold',12,'bold'),relief=RIDGE,bd=5, width=40, textvariable=seller_aadhar)
    selleraadhar.grid(row=1,column=1,pady=10)

    sellerprice=Label(S1,text='Car Price(Rs) :',font=('Arial Bold',15,'bold'),fg='black',bg=bg_color)
    sellerprice.grid(row=2,column=0,padx=30,pady=10)
    sellerprice=Entry(S1,font=('Arial Bold',12,'bold'),relief=RIDGE,bd=5, textvariable=seller_price, width=40)
    sellerprice.grid(row=2,column=1,pady=10)

    carcondition=Label(S1,text='Condition',font=('Arial Bold',15,'bold'),fg='black',bg=bg_color)
    carcondition.grid(row=3,column=0,padx=30,pady=10)

    combo_condition=ttk.Combobox(S1,font=('times new rommon',12),state='readonly',textvariable=seller_condition)
    combo_condition['value']=('< 2 Years','2-5 Years','> 5 Years')
    combo_condition.grid(row=3,column=1,pady=10)

    sellermodelname=Label(S1,text='Model Name :',font=('Arial Bold',15,'bold'),fg='black',bg=bg_color)
    sellermodelname.grid(row=4,column=0,padx=30,pady=10)
    sellermodelname=Entry(S1,font=('Arial Bold',12,'bold'),relief=RIDGE,bd=5,textvariable=seller_modelname, width=40)
    sellermodelname.grid(row=4,column=1,pady=10)

    sellerbankno=Label(S1,text='Bank No :',font=('Arial Bold',15,'bold'),fg='black',bg=bg_color)
    sellerbankno.grid(row=5,column=0,padx=30,pady=10)
    sellerbankno=Entry(S1,font=('Arial Bold',12,'bold'),relief=RIDGE,bd=5,textvariable=seller_bankno, width=40)
    sellerbankno.grid(row=5,column=1,pady=10)

    sellercontactno=Label(S1,text='Contact No :',font=('Arial Bold',15,'bold'),fg='black',bg=bg_color)
    sellercontactno.grid(row=6,column=0,padx=30,pady=10)
    sellercontactno=Entry(S1,font=('Arial Bold',12,'bold'),relief=RIDGE,bd=5, width=40, textvariable=seller_contactno)
    sellercontactno.grid(row=6,column=1,pady=10)

    sellerdesc=Label(S1,text='Description: ',font=('Arial Bold',15,'bold'),fg='black',bg=bg_color)
    sellerdesc.grid(row=7,column=0,padx=30,pady=10)
    sellerdesc=Text(S1,width=40,height=3,font=('Arial Bold',12),relief=RIDGE,bd=7)
    sellerdesc.grid(row=7,column=1,pady=5)
    
    #==========================Right frame================
    S2=Frame(aqua_screen,bg=bg_color,relief=RIDGE,bd=15)
    S2.place(x=620,y=80,width=580,height=480)

    lbl_t=Label(S2,text='Product Details',font=('arial 15 bold'),fg='black',bd=7,relief=GROOVE)
    lbl_t.pack(fill=X)

    textarea=Text(S2,font='arial 14')
    textarea.pack(fill=BOTH)

    #===================Buttons=================
    S3=Frame(aqua_screen,bg=bg_color,relief=RIDGE,bd=15)
    S3.place(x=8,y=550,width=1200,height=100)

    btn1=Button(S3,text='Add',font='arial 20 bold',bg='navy blue',fg='white',width=10, cursor="hand2", command=add)
    btn1.grid(row=0,column=0,padx=25,pady=7)

    btn2=Button(S3,text='Review',font='arial 20 bold',bg='blue',fg='white',width=10, cursor="hand2", command=save)
    btn2.grid(row=0,column=1,padx=25,pady=7)

    btn3=Button(S3,text='Reset',font='arial 20 bold',bg='blue',fg='white',width=10, cursor="hand2",command=reset)
    btn3.grid(row=0,column=2,padx=25,pady=7)

    btn4=Button(S3,text='Cancel',font='arial 20 bold',bg='blue',fg='white',width=10, cursor="hand2",command=cancel)
    btn4.grid(row=0,column=3,padx=25,pady=7)

    btn5=Button(S3,text='Exit',font='arial 20 bold',bg='blue',fg='white',width=10, cursor="hand2",command=exit)
    btn5.grid(row=0,column=4,padx=25,pady=7)

def settingscreen():
    clear(aqua_screen)
    global data1f
    global sl
    global sa
    salesfn()
    #=====================Heading=======================
    title=Label(aqua_screen,text='Dashboard',bg=bg_color,fg='white',font=('Arial Bold',35,'bold'),relief=GROOVE,bd=12)
    title.pack(fill=X)

    #====================left frame details===================
    S1=Frame(aqua_screen,bg=bg_color,relief=RIDGE,bd=15)
    S1.place(x=5,y=83,width=1190,height=300)

    picframe=Frame(S1,bg=bg_color)
    picframe.place(x=660,y=0,width=500,height=270)

    image= Label(picframe, bd=0, bg=bg_color,fg='black',image=img,width=500,height=250 )
    image.place(x=20,y=10)

    carnamev=Label(S1, text='Model Name', font=('Helvetic',15, 'bold','underline'), fg='black',bg=bg_color)
    carnamev.grid(row=0,column=0,padx=20,pady=15)

    c1=0
    r1=0
    while c1<3:
        a=sl[c1][0]
        r1=r1+1
        carname=Label(S1, text=a, font=('Helvetic',15, 'bold'), fg='black',bg=bg_color)
        carname.grid(row=r1,column=0,padx=20,pady=15)
        c1=c1+1

    carprice=Label(S1, text='Car Name', font=('Helvetic',15, 'bold','underline'), fg='black',bg=bg_color)
    carprice.grid(row=0,column=1,padx=20,pady=15)

    c2=0
    r2=0
    while c2<3:
        a1=sl[c2][1]
        r2=r2+1
        carprice=Label(S1, text=a1, font=('Helvetic',15, 'bold'), fg='black',bg=bg_color)
        carprice.grid(row=r2,column=1,padx=20,pady=15)
        c2=c2+1
    
    carprice=Label(S1, text='Car Price', font=('Helvetic',15, 'bold','underline'), fg='black',bg=bg_color)
    carprice.grid(row=0,column=2,padx=20,pady=15)

    c3=0
    r3=0
    while c3<3:
        a2=sl[c3][2]
        r3=r3+1
        carsales=Label(S1, text=a2, font=('Helvetic',15, 'bold'), fg='black',bg=bg_color)
        carsales.grid(row=r3,column=2,padx=20,pady=15)
        c3=c3+1
        
    carsale=Label(S1, text='Total No of Sales', font=('Helvetic',15, 'bold','underline'), fg='black',bg=bg_color)
    carsale.grid(row=0,column=3,padx=20,pady=15)
    
    c4=0
    r4=0
    while c4<3:
        a3=sl[c4][3]
        r4=r4+1
        carsales=Label(S1, text=a3, font=('Helvetic',15, 'bold'), fg='black',bg=bg_color)
        carsales.grid(row=r4,column=3,padx=20,pady=15)
        c4=c4+1
    data1= " SELECT modelname FROM cardata;"
    cursor.execute(data1)
    sa=cursor.fetchall()
    
    S3=Frame(aqua_screen,bg=bg_color,relief=RIDGE,bd=15)
    S3.place(x=5,y=385,width=1190,height=260)

    totalcarframe=Frame(S3,bg="Blue")
    totalcarframe.place(x=10,y=10,width=350,height=200)

    totalcarlabel=Label(totalcarframe, text='Total No Of Cars', font=('Helvetic',12, 'bold'), fg='white',bg="Blue")
    totalcarlabel.place(x=10,y=7)

    totalcarlabel1=Label(totalcarframe, text=len(sl), font=('Helvetic',20, 'bold'), fg='white',bg="Blue")
    totalcarlabel1.place(x=160,y=85)

    totalcarleft=Frame(S3,bg="Blue")
    totalcarleft.place(x=405,y=10,width=350,height=200)

    totalcarleftlabel=Label(totalcarleft, text='Pending Request for selling', font=('Helvetic',12, 'bold'), fg='white',bg="Blue")
    totalcarleftlabel.place(x=10,y=7)

    totalcarleftlabel1=Label(totalcarleft, text=len(sa), font=('Helvetic',20, 'bold'), fg='white',bg="Blue")
    totalcarleftlabel1.place(x=160,y=85)

    totalearning=Frame(S3,bg="Blue")
    totalearning.place(x=800,y=10,width=350,height=200)

    totalearninglabel=Label(totalearning, text='Total Assest ', font=('Helvetic',12, 'bold'), fg='white',bg="Blue")
    totalearninglabel.place(x=10,y=7)

    totalearninglabe1=Label(totalearning, text=totalprice, font=('Helvetic',20, 'bold'), fg='white',bg="Blue")
    totalearninglabe1.place(x=90,y=85)

main()
aqua_screen.mainloop()
cursor.close()
mycon.close()

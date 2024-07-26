# Instal zomoto app
from abc import ABC,abstractmethod
class order(ABC):
    @abstractmethod
    def location(self):
        pass
    @abstractmethod
    def language(self):
        pass
print("WELCOME TO ZOMATO ")
class zomato(order):
  def location(self):
    print(" Access this device's location:Choose Allow or Dismiss")
    b="allow"
    location=input("Access:")
    if location==b:
         print("select your language:")
    else:
        print("Please access your location")
class zomato1(zomato):
   def language(self):
       b="1.english","2.hindi","3.telugu","4.kananada","5.tamil","6.malayalam","7.bengali"
       print(*b,sep="\n")
       language="english","hindi","telugu","kananada","tamil","malayalam","bengali"
       a=input("language:")
       if a in language:
         print("proceed")
       else:
          print("choose your language")
class zomato2(zomato1):
    def phonenumber(self):
        phoneno=input("enter a valid 10 digit phone number:")
        if len(phoneno)==10:
           otp=input("enter your otp number:")
        else:
          print("enter the correct digit")
        if len(otp)==6:
          print("submit")
        else:
           print("invalid otp")
        print("SUCCESSFULLY LOGIN ")
        print("ORDER YOUR FOOD:")
class zomato3(zomato2):
    def food(self):
        c="1.itly","2.dosa","3.poori","4.pongal","5.vadai","6.ravadosa"
        print(*c,sep="\n")
        food="itly","dosa","poori","pongal","vadai","ravadosa"
        d=input("SEARCH YOUR FOOD:")
        if d in food:
           print("Choose Your HOTEL:")
class zomato4(zomato3):
    def hotel(self):
        list="* Copper Kitchen","* Southern Spice","* A2B","* Anand bhavan","* Laskmi Bhavan ", "* Vasantha Bhavan","* Pathma hotel"
        print(*list,sep="\n")
        H="Copper Kitchen","Southern Spice","A2B","Anand bhavan","Laskmi Bhavan ", "Vasantha Bhavan","Pathma hotel"
        e=input("CHOOSE THE HOTEL:")
        if e in H:            
            print("choose your dish :")
        else:
            print("Please select your dish")
        print("Add your dishes")
        v=input("Enter your door number:")
        s=input("landmark:")
        print("confirm address")
        print("GOOGLE PAY UPI")
        print("choose any one of the below option: ")
        pay="1.Google Pay UPI","2.Add Credit or Debit Card","3.Add new UPI Id","4.Paytm","5.Net Banking","6.Cash on Delivery"
        print(*pay,sep="\n")
        payment="google pay UPI","add credit or debit card","add new UPI id","paytm","net banking","cash on delivery"
        f=input("select one of the option:")
        if f in payment:
            z=int(input("enter your pin number:"))
            print("Your order is Placed.")
        
        
obj=zomato4()
obj.location()
obj.language()
obj.phonenumber()
obj.food()
obj.hotel()




    


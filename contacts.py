class Contacts:
    def __init__(self,name,phone_number,email,):
        self.name=name
        self.phone_number=phone_number
        self.email=email

contact1=Contacts("Umid","+998919208091","umid@gmail.com",)
contact2=Contacts("Sunnatillo","+998918202807","sunic@gmail.com")
contact3=Contacts("Ixtitor","+998905442378","ixti@gmail.com")

baza=[contact1,contact2,contact3]

def view_contacts(s:list):
    contact=0
    for i in s:
        contact+=1
        print(f'{contact}-contact \n name:{i.name},\n phone_number:{i.phone_number},\n email:{i.email}')
        print("----------------------------------------")

view_contacts(baza)

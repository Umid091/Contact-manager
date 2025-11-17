import re


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
        print("---------------------------------3"
              "")

# view_contacts(baza)


def add_contacts(s: list):
    name = input("name: ")
    phone_number = input("phone_number: ")
    email = input("email: ")

    if (
            re.fullmatch(r"^[A-Za-z]{2,25}$", name) and
            re.fullmatch(r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$", phone_number) and
            re.fullmatch(r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+", email)
        ):
            print("✔ Hammasi to‘g‘ri  kontakt qo‘shildi")
            contact=Contacts(name, phone_number, email)
            s.append(contact)

    else:
        print("❌ Ma'lumotlar noto‘g‘ri Kontakt qo‘shilmadi!!!!!!!")

# add_contacts(baza)
# view_contacts(baza)

def update_contact(s:list):
    serch_name=input("Tahrirlash uchun contakt ismini kiriting:")
    for i in s:
        if i.name==serch_name:
            print("Qaysi parametrni tahrirlamoqchisiz \n 1.name \n 2.phone_number \n 3.email ")
            tanlov=input("tanlovni kiriting(1/2/3):")
            if tanlov=="1":
                new_name=input("new_nameni kiriting:")
                if re.fullmatch(r"^[A-Za-z]{2,25}$",new_name):
                    i.name=new_name
                    print("✔ name muvaffaqiyatli yangilandi!!!")
                else:
                    print("❌ new_name  noto'g'ri formatda")
            elif tanlov=="2":
                new_phone_number=input("new_phone_number ni kiriting:")
                if re.fullmatch(r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$",new_phone_number):
                    i.phone_number=new_phone_number
                    print("✔ phone_number muvaffaqiyatli yangilandi!!!")
                else:
                    print("❌ new_phone_number noto'g'ri formatda")
            elif tanlov=="3":
                new_email=input("new_email ni kiriting:")
                if re.fullmatch(r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+",new_email):
                    i.email=new_email
                    print("✔ email muvaffaqiyatli yangilandi!!!")
                else:
                    print("❌new_email noto'g'ri formatda")
            else:
                print("❌ bu noto'g'ri tanlov")
            return

    print("❌ Bunday  ism bo'yicha contact topiladi ")


# update_contact(baza)
# view_contacts(baza)

def delete_contact(s:list):
    serch_name = input(" O'chirmoqchi bo'lgan name ni kiring: ")
    for i in range(len(s)):
        if s[i].name==serch_name:
            s.pop(i)
            print("✔ contact muvofaqiyatli o'chirildi")
            return

    print("❌bunday kontak topolmadi")
# delete_contact(baza)
# view_contacts(baza)

def contact_manger(s:list):
    while True:
        kod=input("Qanday amal bajarmoqchisiz \n 1.view_contacts> \n 2.add_contacts> \n 3.update_contact> \n 4.delete_contact>")
        if kod=="1":
            view_contacts(s)
        elif kod=="2":
            add_contacts(s)
        elif kod=="3":
            update_contact(s)
        elif kod=="4":
            delete_contact(s)
        else:
            break
contact_manger(baza)













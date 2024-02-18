# Прошу вибачення ,не встиг додати нормальні коменти до коду ((

from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
        pass

class Phone(Field):
		pass

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self,ph_num_to_add):
        if len(ph_num_to_add)== 10:
            self.phones.append(Phone(ph_num_to_add))
        else:
            print("Phonenumber has invalid format")

    def remove_phone(self,ph_num_to_del):
        if len(ph_num_to_del)== 10:
            pos=0
            for n_del in self.phones:
                if ph_num_to_del == n_del.value:
                    self.phones.pop(pos)
                else:
                    pos +=1
            print(f"No < {ph_num_to_del} > in this contact")
        else:
            print("Phonenumber has invalid format")

    def edit_phone(self,*args):
        for a in args:
            if len(a)== 10:
                self.phones.append(Phone(a))
            else:
                print("Phonenumber has invalid format") 

    def find_phone(self,str_nb):
        for n in self.phones:
            if n.value == str_nb:
                return str_nb                  
        print(f"Contact {self.name} doesn`t consists {str_nb}")
    
class AddressBook(UserDict):
        def add_record(self,cont):
              self.data.update([(cont.name,cont)])
        def show_all(self):
            for name, record in self.data.items():
                print(record)    
        def find(self,nm):
                for name, record in self.data.items():
                    if name.value == nm :
                        return record
                print(f"No < {nm} > contact in the phonebook")
        def delete(self,nm):
            for name, record in self.data.items():                
                if name.value == nm :
                    n_del = name
            try:         
                self.data.pop(n_del)
            except Exception:
                print(f"No < {nm} > contact in the phonebook") 
         
book=AddressBook()

jul_record = Record("John")
jul_record.add_phone("1234567890")
jul_record.add_phone("5555555555") 
book.add_record(jul_record)


jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

john = book.find("John")
john.edit_phone("1234567890", "1112223333")



for name, record in book.data.items():
    print(record)

# Спосіб виведення контактів завдяки  методу самої тел.книги
book.show_all() 

found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  

book.delete("Jane")

book.show_all()

jul_record = Record("Jul")
jul_record.add_phone("1234567890")
jul_record.add_phone("5555555000") 
book.add_record(jul_record)

book.show_all()

jul_record.remove_phone("1234567891") # спроба видалити неіснуючий номер
jul_record.remove_phone("1234567890")
book.add_record(jul_record)
book.show_all()
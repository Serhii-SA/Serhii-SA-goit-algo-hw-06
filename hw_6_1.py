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

    def add_phone(self,ph):
        if len(ph)== 10:
            self.phones.append(Phone(ph))
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
              
         
book=AddressBook()

john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555") 
book.add_record(john_record)


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

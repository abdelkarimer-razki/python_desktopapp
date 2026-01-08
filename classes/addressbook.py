from classes.contact import contact
import json

class AddressBook:
    def __init__(self):
        self.filename = "./docs/AddressBook.json"
        try:
            with open(self.filename, "r") as file:
                self.list = json.load(file)
        except:
            self.list = []

    def add(self, nom, email, phone):
        try:
            with open(self.filename, "r") as file:
                self.list = json.load(file)
        except:
            self.list = []
        self.list.append(contact(nom, email, phone).__dict__)
        with open(self.filename, "w") as file:
            json.dump(self.list, file, indent=4)
    
    def delete(self, id):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
            
            data = [contact for contact in data if contact["id"] != id]
            self.list = data
            with open(self.filename, "w") as file:
                json.dump(data, file, indent=4)
        except:
            print("No contact is yet stored")
    
    def modifier(self, id, nom, email, phone):
        with open(self.filename, "r") as file:
            data = json.load(file)
        
        for contact in data:
            if contact["id"] == id:
                contact['nom'] = nom
                contact['email'] = email
                contact['phone'] = phone
        self.list = data
        with open(self.filename, "w") as file:
            json.dump(self.list, file, indent=4)

    def show(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
        except:
            print("No contact is yet stored")
        print(data)
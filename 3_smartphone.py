class Phone():
    def __init__(self):
        self.contacts = []

    def add_contact(self, name):
        if name not in self.contacts:
            self.contacts.append(name)
        else:
            print("Name already in contacts!")
        
        

    def remove_contact(self, name):
        if name in self.contacts:
            self.contacts.remove(name)
        else:
            print("Name not in contacts!")
        
    
    def make_call(self, name):
        if name in self.contacts:
            print(f"Calling {name}...")
        else:
            print("Name not in contacts!")


class Camera():
    def take_pic(self):
        print("The picture was taken successfully")



class Smartphone(Phone, Camera):
    pass
    

# Example

ph = Smartphone()

ph.add_contact("Mahmoud")
ph.make_call("Mahmoud")
ph.take_pic()
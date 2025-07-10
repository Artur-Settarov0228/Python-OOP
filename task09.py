class User:
    def __init__(self , username, email, is_active):
        self.username = username
        self.email = email
        self.is_active = is_active

    def activate(self):
        self.is_active = True
        print(f"{self.username} faollashtirildi ")

    def deactivate(self):
        self.is_active = False
        print(f"{self.username} bloklandi ")

p_1 =User("artue05" , "artur00@gmail.com" ,False)

p_1.activate()
p_1.deactivate()

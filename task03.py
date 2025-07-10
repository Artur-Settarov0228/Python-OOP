class User:
    def __init__(self, username, email , is_active):
        self.username = username
        self.email = email
        self.is_active = is_active

user_1 = User("Artur05","settarovartur0@gmail.com" , True)
print(f"{user_1.username}, {user_1.email} , {user_1.is_active}")
        
class Book:
    def __init__(self , title ,  outhor , is_read=False):
        self.title = title
        self.outhor = outhor
        self.is_read = is_read
        
    def mark_as_read(self ):
        self.is_read = True
        print(f"Kitob uqilgan deb belgilanadi")

    def status(self):
        if self.is_read:
            print("oqilgan")
        else:
            print("oqilmagan")

book_1 = Book("Eyinshten pasulatlar" , "Paulo Coelho")

book_1.mark_as_read()
book_1.status()
book_1.status()


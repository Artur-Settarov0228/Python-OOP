class Book:
    def __init__(self , title ,author , is_read=False):
        self.title = title
        self.author = author
        self.is_read = is_read


    def mark_as_read(self):
        self.is_read = True
        print(f"{self.title} - Kitob uqilgan deb hisoblandi ")

    def status(self):
        if self.is_read:
            print(f"{self.title} - oqilgan")
        else:
            print(f"{self.title} - oqilmagan")

book_1 = Book("Shum bola" , "G'ofur G'ulom")
book_2 = Book("Ikki eshik orasi" , "o'tkir Hashimov")  
book_3 = Book("Alkimyogar", "Paulo Coelho")
book_4 = Book("Sherlok Xolmos" , "Artur ......")

book_1.mark_as_read()
book_4.mark_as_read()

book_1.status()
book_2.status()
book_3.status()
book_4.status()
        
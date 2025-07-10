class Movie:
    def __init__(self , titile, genre, duration, rating):
        self.title = titile
        self.genre = genre
        self.duration = duration
        self.rating = rating

    def show_summary(self):
        print(f"{self.title} — {self.genre} janridagi film. Reyting: {self.rating}/10.")   

movei_1 =Movie("Thor" , "fantastic", 150 , 8.8) 

movei_1.show_summary()
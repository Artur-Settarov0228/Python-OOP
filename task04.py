class Movie:
    def __init__(self , titile, genre, duration, rating):
        self.title = titile
        self.genre = genre
        self.duration = duration
        self.rating = rating

movie_1 = Movie("Thor" , "fantastic", 150 , 8.8)
print("Kinoni nomi:" , movie_1.title)
print("Janri :" , movie_1.genre)
print("kinoni vaqti : " , movie_1.duration)
print("IMDB reytingi:", movie_1.rating)        
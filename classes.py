# 1
class Movie():
    def __init__(self, title, year, gender, rate):
        self.title = title
        self.year = year
        self.gender = gender
        self.rate = rate

    def details(self):
        print(f'Filme: {self.title} | Ano: {self.year} | Gênero: {self.gender} | Nota: {self.rate}/5')

movie1 = Movie('Interestelar', 2014, 'Ficção Científica', 4.7)
movie2 = Movie('Matriz', 2000, 'Ficção Científica', 4.5)

movie1.details()
movie2.details()
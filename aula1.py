# Mini ecercício 1
my_movies = [
    'Matrix',
    'Avatar',
    'Star Wars',
    'Vingadores'
]

print(my_movies[2])

my_movies.append('Moana')
my_movies.remove(my_movies[2])

for movie in my_movies:
    print('Filme: ', movie)

# 2
my_profile = {
    'name': 'Mané',
    'age': 14,
    'city': 'Pedra Dourada',
    'hobbie': ['subir montanhas', 'jogar xadrez', 'viajar']
}

print(f'Oi, meu nome é {my_profile['name']} e eu moro em {my_profile['city']}. Gosto de {my_profile['hobbie'][0]}, {my_profile['hobbie'][1]} e {my_profile['hobbie'][2]}') 
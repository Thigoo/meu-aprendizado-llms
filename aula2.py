# 1
my_friends = [
    'João',
    'Breno',
    'Maurício',
    'Josi',
    'Camila'
]

starts_with_j = [n for n in my_friends if n.startswith('J')]
starts_with_m = [n for n in my_friends if n.startswith('M')]

# print(starts_with_j, starts_with_m)

all = starts_with_m + starts_with_j

# print(all)

# 2
my_profile = {
    'name': 'Mané',
    'age': 14,
    'city': 'Pedra Dourada',
    'hobbie': ['subir montanhas', 'jogar xadrez', 'viajar']
}

my_profile.update({
    'job': 'IA student',
    'team': 'Flamengo'
})

my_profile['favorite_color'] = 'laranja'
for key, value in my_profile.items():
    print(key, ':', value)

print(my_profile)
favorite_color = my_profile.get('favorite_color', 'Não informado')
print(favorite_color)


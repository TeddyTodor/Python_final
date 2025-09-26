import tabulate
def exo_1 () :
    my_int = 3
    my_float = 4.1
    my_str = "chocolat"

    my_list = [my_int,my_float,my_str]

    for index in range (len(my_list)) :
        print(f"index {index} : {my_list[index]}")

#exo_1()

my_dico = {1 : "un",
        2 : "deux",
        3 : "trois",
        "quatre" : 4,
        "cinq" : 5}

key = 1

def exo_2 (key, my_dico : dict) -> None:
    print(f"Pour la cle {key}, voici la valeur correspondante {my_dico[key]}")

def generate_value () :
    i = 1
    while True :
        yield i**2
        i+=1

generator = generate_value()
M = tabulate.tabulate([[next(generator) for i in range (10)] for j in range (10)])
print (M)
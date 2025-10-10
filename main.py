def generate_value () :
    k = 1
    while True:
        yield 2**k
        k+=1

def generate_dico () :

    generator = generate_value()
    my_keys = [i for i in range (6, 71, 1)]
    my_values = [next(generator) for _ in range (len(my_keys))]

    my_dico = {}

    for i in range (len(my_keys)) :
        current_key = f"keys_{my_keys[i]}"
        current_value = my_values[i]
        my_dico[current_key] = current_value

    return(my_dico)

new_dico = generate_dico()

def print_pairs () :

    for key in new_dico.keys() :
        corresponding_value = new_dico[key]
        pretty_sentence = f"For the {key}, here is the corresponding value {corresponding_value}"
        print(pretty_sentence)   

def exo_1_try_except (a:int,b:int) :

    try :
        c = a/b
        print(f"YEP : {c}")
    except ZeroDivisionError :
        print("Attention ZeroDivisionError")
    except :
        print ("Error 404")
    finally : 
        print ("Ohg Anyway")


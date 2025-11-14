
def generate_value () :
    k = 1
    while True :
        yield 2**k 
        k += 1

def exo():
    generator = generate_value()
    nb_elements = 10
    my_dico = {}

    my_keys = [f"keys_{i}" for i in range (nb_elements)]
    my_vals = [next(generator) for _ in range (len(my_keys))]

    for index in range (len(my_keys)) :
        current_key = my_keys[index]
        current_value = my_vals[index]
        my_dico[current_key] = current_value

    for keys in my_dico :
        #print (f"For the {keys} the value is : {my_dico[keys]}")
        pass
    return my_dico

def test () :

    my_dico = exo()

    print("MAIN - Started")

    try :
        with open("logs/test.log", "a") as file :
            for keys in my_dico :
                file.write(f"For the {keys} the value is : {my_dico[keys]}\n")

    except Exception as e:
        with open("logs/error.log", "a") as file :
            file.write(f"ERROR - {e}\n")

    finally :
        pass

def bin() :
    with open("logs/test.log", "w") as file :
        file.write(f"")

    with open("logs/error.log", "w") as file :
        file.write(f"")

#Generates a value n**2 
def generate_value () :
    k = 0
    while (True) :
        yield(k**2)

#Creates a dictionary and fills it up with {"key_n", n**2}
def generate_dico (nb_elements : int) :

    generator = generate_value()


    my_keys = [f"key_{i}" for i in range (nb_elements)]
    my_vals = [next(generator) for _ in range (nb_elements)]

    my_dico = {}
    my_dico_manual = {1 : 2,
            2 : 1}

    for i in range (nb_elements) :
        current_key = my_keys[i]
        current_val = my_vals[i]
        my_dico[current_key] = current_val

    for keys in my_dico.keys() :
        #print(f"For the {keys}, the value is : {my_dico[keys]}")
        pass

    return my_dico


def unit_test() :

    my_new_dico = generate_dico(10)
    testing_keys = ["key_0", "1", 1, generate_value, generate_dico(2), Exception, {243 : 45, 456 : 12}]

    for i in range (len(testing_keys)) :
        current_testing_key = testing_keys[i] 
        
        try :
            corresponding_testing_value = my_new_dico[current_testing_key]
            with open("logs/test.log", "a") as file :
                file.write(f"TESTING - For the key : {current_testing_key} here is the corresponding value : {corresponding_testing_value}\n")

        except Exception as e :
            with open("logs/error.log", "a") as file :
                file.write(f"ERROR - {e}\n")


def break_continue (j : int, max_threshold : int) :
    while j != max_threshold :
        j += 1
        print(f"En résumé : j : {j}")
        for i in range(10) :
            if j%2 == 0 or i%2 == 0 :
                continue
            if i >= 5 :
                break
                
            print (f"       j_{j} : i_{i}")


#Errors
    #SyntaxError : Vous avez mal écrit le code, python n'arrive as a le lire
    #TypeError : Bien écrit mais n'as aucun sens (Ex : 3 + "x")
    #ValueError : Bien écrit mais la valeur donnée n'as aucun sens

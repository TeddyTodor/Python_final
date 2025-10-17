def generate_value () :
    local_k = 0
    while True:
        yield 2**local_k
        local_k+=1

generator = generate_value()
nbr_element = 25

my_keys = [f"key_{i + 1}" for i in range(nbr_element)]
my_values = [f"value_{next(generator)}" for _ in range (nbr_element)]

my_dico = {}

for index in range (nbr_element) :
    current_key = my_keys[index]
    current_value = my_values[index]
    my_dico[current_key] = current_value

count = 0
for key in my_dico.keys() :
    corresponding_value = my_dico[key]
    pretty_sentence = f"For the {key}, here is the corresponding {corresponding_value}\n"
    try :
        with open("output.txt", "a") as file: 
            file.write (pretty_sentence)
    except :
        with open("error.txt", "a") as err_file: 
            err_file.write("ERROR, COULD NOT PRINT PRETTY_SENTENCE")
    finally :
        count += 1
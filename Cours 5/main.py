def generate_value() :
    k = 1
    while True :
        yield 2**k
        k += 1

nb_of_values = 10
my_dico = {}

generator = generate_value()

my_keys = [f"key_{i}"  for i in range (nb_of_values)]
my_vals = [next(generator) for _ in range (nb_of_values)]

for i in range (nb_of_values) :
    current_key = my_keys[i]
    current_value = my_vals[i]
    my_dico[current_key] = current_value

for keys in my_dico :
    print(f"{keys} : {my_dico[keys]}")

try :
    answer = int(input("Donne une valeure : "))
    with open("Logs/test.log" , "a") as file :
        file.write(f"{answer} \n")
except Exception as e:
    with open("Logs/error.log", "a") as file :
        file.write(f"ERROR - {e} \n")
finally :
    print("Script finished")

finished = True
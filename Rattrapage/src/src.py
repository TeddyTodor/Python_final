def data_reader (file) :

    with open(file, "r") as f :
        data = f.readlines()
    dico = {}
    for line in data :
        new_data = line.split(",")
        dico [new_data[0]] = new_data[1], new_data[2]
    return dico


dico = data_reader("data/data.txt")   
print(dico)    

def data_process (dico : dict) :
    for key in dico.keys() :
        data_list = dico[key]
        age = int(data_list[1])
        name = data_list[0]
        if (age >= 18 ) :
            state = "major"
        else :
            state = "minor"
        dico[key] =  name, age, state

    return dico

dico = data_process(dico)
print(dico)

def data_save () :
    with open("data/new_data.txt", "w") :
        pass
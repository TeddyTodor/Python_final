data_path = "data/data.txt"

my_dico = {}

with open (data_path, "r") as f :
    all_lines_list = f.readlines()
    for index in range (len(all_lines_list)) :
        current_line = all_lines_list[index].removesuffix("\n")
        temp_data = current_line.split(";")
        #print(data)

        data_id = int(temp_data[0])
        data_age = int(temp_data[1])
        data_name = temp_data[2]
        data_gender = int(temp_data[3])
        data_hobby = temp_data[4]
    
        data = [data_age,data_name, data_gender, data_hobby]
        my_dico[data_id] = data

for key in my_dico.keys() :
    corresponding_value = my_dico[key]
    print(f"{key} : {corresponding_value}")

    #Age incrementation
    corresponding_value[1] += 1
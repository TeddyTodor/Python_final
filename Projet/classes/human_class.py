class Human () :

    def __init__(self, id, firstname, lastname, age, economy, gender):

        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.economy = economy
        self.gender = gender

        self.parent_dict = {}

    def introduce_yourself(self) :

        pretty_sentence = f"""Hi I am :
        ID : {self.id}
        Full name : {self.lastname} {self.firstname}
        age : {self.age}
        economy : {self.economy}
        gender : {self.gender}"""#parent_list : {self.parent_list}

        with open("logs/human.log", "a") as f :
            f.write(pretty_sentence + "\n")

class Parent (Human) :

    def __init__(self, id, firstname, lastname, age, economy, gender):

        super().__init__(id, firstname, lastname, age, economy, gender)

        self.child_list = []
        self.salary = 0
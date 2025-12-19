class Human () :

    def __init__(self, id, firstname, lastname, age, economy, gender, x = 0, y = 0):

        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.economy = economy
        self.gender = gender

        self.parent_dict = {}
        self.x = 0
        self.y = 0

    def move (self, dx, dy) :
        self.x += dx
        self.y += dy
    
    def live_one_day (self) :
        from random import randrange
        self.economy -= randrange(0, 8)
        self.move(randrange(-5, 6), randrange(-5, 6))

    def introduce_yourself(self, output_filename = "logs/human.log") :

        pretty_sentence = f"{self.id}/{self.firstname}/{self.lastname}/{self.age}/{self.economy}/{self.gender}/{self.x}/{self.y}"

        with open(output_filename, "a") as f :
            f.write(pretty_sentence + "\n")

class Parent (Human) :

    def __init__(self, id, firstname, lastname, age, economy, gender):

        super().__init__(id, firstname, lastname, age, economy, gender)

        self.child_list = []
        self.salary = 0

class Human_factory () :
    def __init__(self):
        self.human_dict = {}

    def generate_humans (self, filepath : str = "data/humans_data.txt") :
        with open(filepath, "r" ) as f :
            for line in f.readlines() :
                data = line.split("/")
                id = int(data[0])
                firstname = data[1]
                lastname = data[2]
                age = int(data[3])
                economy = int(data[4])
                gender = data[5].removesuffix("\n")
                #x = int(data[6])
                #y = int(data[7].removesuffix("\n"))

                new_human = Human(id, firstname, lastname, age, economy, gender)
                self.human_dict[new_human.id] = new_human
    def live_one_day (self) :
        for key in self.human_dict.keys() :
            current_human = self.human_dict[key]
            if isinstance (current_human, Human) :
                current_human.live_one_day

    def live_one_week (self) :
        for _ in range (7) :
            self.live_one_day()

    def save_human_data(self, output_file = "output_data.txt") :
        for key in self.human_dict.keys() :
            current_human = self.human_dict[key]
            if isinstance (current_human, Human) :
                current_human.introduce_yourself(output_file)       
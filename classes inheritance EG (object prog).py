class Creature: # this is the PARENT CLASS
    def __init__(self, name):
        self.name = name

    def battle(self):
        print(f"{self.name} enters the gym and starts a battle.")


class Trainer(Creature): # this is a CHILD CLASS
    def __init__(self, name, how_many_caught):
        super().__init__(name)
        self.how_many_caught = how_many_caught

    def catch(self):
        print(f"{self.name} is catching them all! But he's only caught {self.how_many_caught} so far.")


class Pokemon(Creature): # this is a CHILD CLASS
    def __init__(self, name, pokemon_type, first_evolution):
        super().__init__(name)
        self.pokemon_type = pokemon_type
        self.first_evolution = first_evolution

    def evolve(self):
        print(f"{self.name} is a {self.pokemon_type} type pokemon and just evolved into a {self.first_evolution}!")


ash = Trainer("ash", 10)
pikachu = Pokemon("pikachu", "electric", "raichu")

ash.battle()
ash.catch()
pikachu.battle()
pikachu.evolve()
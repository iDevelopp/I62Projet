import enemy_unit

class Situation:
    def __init__(width,height):
        self.OF_units = []
        self.BF_units = []

    def add_entity(type, pos):
        match type:
            case "OF_R":
                self.OF_units.append(OF_R(pos, self))
